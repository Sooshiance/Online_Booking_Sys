from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter

from .models import Post


class AdminComment(admin.ModelAdmin):
    list_display = ['user', 'title', 'admin_approval', 'vote']
    search_fields = ['user', 'title']
    list_display_links = ['user', 'title']
    list_filter = (('created_at', JDateFieldListFilter), 'admin_approval')
    sortable_by = ('title', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Post, AdminComment)
