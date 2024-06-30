from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': (
            'email', 'password', 'username', 'uuid_google',
            'profile_picture', 'first_name', 'last_name', 'is_active',
            'is_staff', 'is_superuser'
        )}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )
    exclude = ('date_joined',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'uuid_google', 'is_staff', 'is_superuser'),
        }),
    )

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
