from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

from .models import ArrotModel, GolsaModel, Wallet


class ArrotAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'hour', 'admin_approval', 'pk')
    list_filter = (('date', JDateFieldListFilter),
                    ('created_at', JDateFieldListFilter),
                    'admin_approval',)
    sortable_by = ('created_at', 'title')
    readonly_fields = ('created_at', 'updated_at')
    list_display_links = ('user', 'title', 'pk')
    search_fields = ('user', 'title')


class GolsaAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'hour', 'admin_approval', 'pk')
    list_filter = (('date', JDateFieldListFilter),
                    ('created_at', JDateFieldListFilter),
                    'admin_approval',)
    sortable_by = ('created_at', 'title')
    readonly_fields = ('created_at', 'updated_at')
    list_display_links = ('user', 'title', 'pk')
    search_fields = ('user', 'title')


class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'reach_limit']
    list_filter = ['reach_limit']


admin.site.register(ArrotModel, ArrotAdmin)

admin.site.register(GolsaModel, GolsaAdmin)

admin.site.register(Wallet, WalletAdmin)