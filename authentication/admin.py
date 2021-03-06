from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.forms import CustomUserCreationForm, CustomUserChangeForm
from authentication.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'password1',
                'password2', 'is_staff', 'is_active'
            )
        }),
    )
    search_fields = ('email', 'first_name')
    ordering = ('email', 'first_name')


admin.site.register(CustomUser, CustomUserAdmin)
