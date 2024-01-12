from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminModule

from .models import User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(UserAdminModule):
    """
    Custom User Admin module
    """
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    fields = None
    list_display = ["email", "first_name", "last_name", "is_staff"]

    ordering = ["email"]

admin.site.register(User, UserAdmin)

