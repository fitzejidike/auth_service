
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Set admin branding after admin is imported
admin.site.site_header = getattr(settings, "ADMIN_SITE_HEADER", "Django Administration")
admin.site.site_title = getattr(settings, "ADMIN_SITE_TITLE", "Django Admin")
admin.site.index_title = getattr(settings, "ADMIN_INDEX_TITLE", "Welcome to the Admin Portal")

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "full_name", "is_staff", "is_superuser", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "full_name")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password", "full_name")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "password1", "password2", "is_staff", "is_superuser", "is_active"),
        }),
    )

# Set admin branding after admin is imported
admin.site.site_header = getattr(settings, "ADMIN_SITE_HEADER", "Django Administration")
admin.site.site_title = getattr(settings, "ADMIN_SITE_TITLE", "Django Admin")
admin.site.index_title = getattr(settings, "ADMIN_INDEX_TITLE", "Welcome to the Admin Portal")

admin.site.register(User, UserAdmin)
