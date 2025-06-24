from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.models import User
from django.db import transaction
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    # CORRECCIÓN: Usamos argumentos con nombre (label="...", help_text="...")
    email = forms.EmailField(
        label="Correo electrónico",
        required=True,
        help_text='Requerido. Ingrese una dirección de correo válida.'
    )
    first_name = forms.CharField(
        label="Nombre", 
        max_length=150, 
        required=False
    )
    last_name = forms.CharField(
        label="Apellido", 
        max_length=150, 
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario registrado con este correo electrónico.")
        return email
    @transaction.atomic

    def save(self, commit=True):
        user = super().save(commit=True)
        # Asegurarnos de que el perfil se cree solo si no existe
        UserProfile.objects.get_or_create(user=user, defaults={'role': 'Lector'})
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['username'].help_text = 'Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.'


class UserUpdateForm(forms.ModelForm):
    # CORRECCIÓN: Usamos 'label' explícitamente aquí también
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }

class PasswordChangeForm(DjangoPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = "Contraseña actual"
        self.fields['new_password1'].label = "Nueva contraseña"
        self.fields['new_password2'].label = "Confirmar nueva contraseña"
