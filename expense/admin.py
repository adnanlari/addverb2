from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Employee


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Employee
    list_display = ['username', 'name', 'mobile']

    fieldsets = (
        (None, {'fields': ('name', 'username', 'mobile')}), )


admin.site.register(Employee, CustomUserAdmin)
# Register your models here.