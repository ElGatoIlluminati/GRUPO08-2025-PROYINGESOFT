from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import UserProfile
from boletines.models import Categoria 
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, Case, When, Value


# Create your views here.

# Esta función verifica si el usuario es un superusuario (administrador)
def is_superuser(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_superuser)
def user_list_view(request):
    # --- Lógica de Búsqueda y Filtro (se mantiene igual) ---
    search_query = request.GET.get('q', '')
    role_query = request.GET.get('role', '')

    # --- NUEVO: Lógica de Ordenamiento ---
    sort_by = request.GET.get('sort', 'username') # Por defecto, ordena por username
    direction = request.GET.get('dir', 'asc')     # Por defecto, dirección ascendente

    # Lista de campos válidos para ordenar para evitar errores
    valid_sort_fields = ['username', 'email', 'userprofile__role']
    if sort_by not in valid_sort_fields:
        sort_by = 'username'

    # Construimos el ordenamiento
    order_prefix = '' if direction == 'asc' else '-'

    # Caso especial para el orden de roles
    if sort_by == 'userprofile__role':
        # Usamos Case/When para asignar un valor numérico a cada rol y ordenar por él
        queryset = User.objects.annotate(
            role_order=Case(
                When(userprofile__role='Administrador', then=Value(1)),
                When(userprofile__role='Editor', then=Value(2)),
                When(userprofile__role='Lector', then=Value(3)),
                default=Value(4) # Para perfiles sin rol o con roles futuros
            )
        ).select_related('userprofile').all()
        # El prefijo de dirección se aplica al campo de orden, no al de rol
        order_field = f"{order_prefix}role_order"
    else:
        queryset = User.objects.select_related('userprofile').all()
        order_field = f"{order_prefix}{sort_by}"

    # Aplicamos los filtros de búsqueda
    if search_query:
        queryset = queryset.filter(
            Q(username__icontains=search_query) | 
            Q(email__icontains=search_query)
        )
    if role_query:
        queryset = queryset.filter(userprofile__role=role_query)

    # Aplicamos el ordenamiento final
    usuarios = queryset.order_by(order_field, 'username') # Añadimos 'username' como 2do criterio

    context = {
        'usuarios': usuarios,
        'role_choices': UserProfile.ROLE_CHOICES,
        'current_search': search_query,
        'current_role': role_query,
        'sort_by': sort_by, # Pasamos los parámetros de orden a la plantilla
        'direction': direction,
    }
    return render(request, 'dashboard/user_list.html', context)

@user_passes_test(is_superuser)
def update_user_role(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        new_role = request.POST.get('role')

        # Validar que los datos necesarios fueron enviados
        if not user_id or not new_role:
            messages.error(request, "Información incompleta para actualizar el rol.")
            return redirect('dashboard:user_list')
        
        # Validar que el rol sea válido
        valid_roles = [role[0] for role in UserProfile.ROLE_CHOICES]
        if new_role not in valid_roles:
            messages.error(request, "El rol seleccionado no es válido.")
            return redirect('dashboard:user_list')

        try:
            user_to_update = User.objects.get(id=user_id)
            # AÑADIMOS ESTA PROTECCIÓN
            if user_to_update.is_superuser:
                messages.error(request, "No se puede cambiar el rol de un superusuario.")
                return redirect('dashboard:user_list')

            user_profile = UserProfile.objects.get(user=user_to_update)
            user_profile.role = new_role
            user_profile.save()
            messages.success(request, f"Se actualizó el rol de {user_profile.user.username} a {new_role}.")
        except User.DoesNotExist:
            messages.error(request, "El usuario no existe.")
        except UserProfile.DoesNotExist:
            messages.error(request, "El usuario no tiene un perfil para actualizar.")
        # ... (el resto del try-except) ...

    return redirect('dashboard:user_list')

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'dashboard/user_confirm_delete.html'
    success_url = reverse_lazy('dashboard:user_list')
    success_message = "El usuario ha sido eliminado exitosamente."

    # Este método asegura que solo los superusuarios puedan acceder a esta vista
    def test_func(self):
        return self.request.user.is_superuser
    
    # Añadimos una validación extra para no poder eliminar a otro superusuario
    # o a uno mismo.
    def get_object(self, queryset=None):
        user_to_delete = super().get_object(queryset)
        if user_to_delete.is_superuser:
            # Puedes manejar esto como quieras, por ejemplo, mostrando un error.
            # Por ahora, simplemente redirigimos.
            messages.error(self.request, "No se puede eliminar a un superusuario desde este panel.")
            return None # Esto causará una redirección o un error 404
        return user_to_delete

    # Sobrescribimos el método post para añadir un mensaje en caso de error
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object is None:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)


# NUEVA VISTA para gestionar categorías
@user_passes_test(is_superuser)
def manage_categories_view(request):
    # Si el admin envía el formulario para crear una nueva categoría
    if request.method == 'POST':
        nombre_categoria = request.POST.get('nombre_categoria')
        if nombre_categoria:
            # Usamos get_or_create para evitar duplicados
            categoria, creada = Categoria.objects.get_or_create(nombre=nombre_categoria.strip())
            if creada:
                messages.success(request, f"Categoría '{categoria.nombre}' creada exitosamente.")
            else:
                messages.warning(request, f"La categoría '{categoria.nombre}' ya existía.")
        else:
            messages.error(request, "El nombre de la categoría no puede estar vacío.")
        return redirect('dashboard:manage_categories')

    # Obtenemos todas las categorías para listarlas
    categorias = Categoria.objects.all().order_by('nombre')
    context = {
        'categorias': categorias
    }
    return render(request, 'dashboard/manage_categories.html', context)

# NUEVA VISTA para eliminar una categoría
@user_passes_test(is_superuser)
def delete_category_view(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        nombre_categoria = categoria.nombre
        categoria.delete()
        messages.success(request, f"Categoría '{nombre_categoria}' eliminada.")
    return redirect('dashboard:manage_categories')

@user_passes_test(is_superuser)
def dashboard_home_view(request):
    # Esta vista simplemente renderiza la página de inicio del dashboard.
    # En el futuro, aquí podríamos mostrar estadísticas o resúmenes.
    return render(request, 'dashboard/dashboard_home.html')