from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm, UserUpdateForm, PasswordChangeForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "¡Registro exitoso! Bienvenido.")
            return redirect('boletines:lista') # Redirige a la lista de boletines
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    # Si el método es POST, procesamos el formulario
    if request.method == 'POST':
        # Creamos una instancia del formulario CON los datos que envió el usuario
        form = AuthenticationForm(request, data=request.POST)
        
        # Verificamos si el formulario es válido (si las credenciales son correctas)
        if form.is_valid():
            # Si es válido, obtenemos el usuario y lo logueamos
            user = form.get_user()
            login(request, user)
            messages.success(request, f"¡Bienvenido de vuelta, {user.username}!")
            return redirect('core:home') # Redirigimos al home
    
    # Si el método es GET (el usuario acaba de llegar a la página)
    # o si el formulario del POST no fue válido, creamos un formulario limpio o pasamos el inválido
    else:
        form = AuthenticationForm()

    # Renderizamos la plantilla, pasándole el formulario
    # (ya sea el nuevo y limpio, o el que contiene los errores)
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('boletines:lista')

@login_required
def perfil_view(request):
    # La lógica para editar y eliminar se manejará en otras vistas
    return render(request, 'perfil.html')

# Las vistas para editar y eliminar perfil las podemos añadir después para no alargar.
# Por ahora, con login, logout y registro tenemos lo esencial.
def perfil_editar_view(request): # Placeholder
    messages.info(request, "Función para editar perfil aún no implementada.")
    return redirect('users:perfil')

def perfil_eliminar_view(request): # Placeholder
    messages.info(request, "Función para eliminar perfil aún no implementada.")
    return redirect('users:perfil')

@login_required
def perfil_view(request):
    # Formulario para actualizar datos del usuario
    if request.method == 'POST' and 'update_profile' in request.POST:
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado exitosamente!')
            return redirect('users:perfil')
    else:
        user_form = UserUpdateForm(instance=request.user)

    # Formulario para cambiar la contraseña
    if request.method == 'POST' and 'change_password' in request.POST:
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Mantiene al usuario logueado
            messages.success(request, '¡Tu contraseña ha sido cambiada exitosamente!')
            return redirect('users:perfil')
    else:
        password_form = PasswordChangeForm(request.user)

    context = {
        'user_form': user_form,
        'password_form': password_form
    }
    return render(request, 'perfil.html', context)


# Usamos una Vista Basada en Clase para eliminar la cuenta, es más seguro y limpio
class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('core:home') # Redirige al home después de borrar
    success_message = "Tu cuenta ha sido eliminada permanentemente."

    def get_object(self, queryset=None):
        # Asegurarnos de que el usuario solo pueda eliminar su propia cuenta
        return self.request.user