from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import *
from .models import *
# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = UserSignupForm

    list_display = ('email', 'username')
    list_filter = ('email', 'is_special_user', 'is_active')
    fieldsets = (
        ('user', {'fields': ('email', 'Password')}),
        ('personal info', {'fields': ('is_admin',)}),
        ('permissions', {'fields': ('is_active',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'username')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()



admin.site.register(User)
admin.site.register(Profile)
