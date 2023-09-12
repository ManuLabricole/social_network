from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'date_joined', 'is_active')
    list_filter = ('is_active', 'date_joined')
    search_fields = ('email', 'name')
    ordering = ('email',)

    # Define custom fieldsets to use your custom fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('name',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )


# Unregister the User model and then re-register with the custom admin class
if admin.site.is_registered(User):
    admin.site.unregister(User)

admin.site.register(User, CustomUserAdmin)
