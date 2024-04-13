from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

from .models import User, Profile


class Admin(UserAdmin):
    list_display = ('phone', 'fullName', 'email', 'is_active', 'pk',)
    filter_horizontal = ()
    list_filter = ('is_active',)
    fieldsets = ()
    search_fields = ('email', 'phone')
    list_display_links = ('phone', 'email')
    # This line below added because 'ordering' attribute need a dependency
    ordering = ('email', 'username')


class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'email', 'pk']
    search_fields = ('phone', 'user')
    sortable_by = ('pk', 'user')


admin.site.register(User, Admin)

admin.site.register(Profile, AdminProfile)
