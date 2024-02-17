from django.contrib import admin

from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	

from .models import ArrotModel, GolsaModel, Wallet


class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
	model = ArrotModel


class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
	model = GolsaModel


class ArrotAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user', 'title', 'hour', 'admin_approval', 'date')
    list_filter = ('admin_approval',)
    sortable_by = ('created_at', 'title')
    readonly_fields = ('created_at', 'updated_at', 'pk')
    list_display_links = ('user', 'title')
    search_fields = ('user__phone', 'title')


class GolsaAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user', 'title', 'hour', 'admin_approval', 'date')
    list_filter = ('admin_approval',)
    sortable_by = ('created_at', 'title')
    readonly_fields = ('created_at', 'updated_at', 'pk')
    list_display_links = ('user', 'title')
    search_fields = ('user__phone', 'title')


class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'reach_limit']
    list_filter = ['reach_limit']
    search_fields = ("user__phone",)


admin.site.register(ArrotModel, ArrotAdmin)

admin.site.register(GolsaModel, GolsaAdmin)

admin.site.register(Wallet, WalletAdmin)
