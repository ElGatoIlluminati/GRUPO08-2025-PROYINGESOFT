from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Define un "inline" para el UserProfile, para que aparezca dentro del User
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'perfiles'

# Define un nuevo User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Vuelve a registrar UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)