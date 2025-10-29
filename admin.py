from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FacultyUser, FacultyAppraisal,Qualification, Experience, Appraisal

# FacultyUser Admin
@admin.register(FacultyUser)
class FacultyUserAdmin(UserAdmin):
    model = FacultyUser
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'is_faculty')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_faculty')
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register other models
admin.site.register(Qualification)
admin.site.register(Experience)
admin.site.register(Appraisal)
admin.site.register(FacultyAppraisal)
