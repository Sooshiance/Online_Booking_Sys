from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter

from .models import Category, AllService, Letter


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'pk')
    list_filter = (('created_at', JDateFieldListFilter),)
    search_fields = ('title', 'slug')


class AllServiceAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'pk',)
    list_filter = (('created_at', JDateFieldListFilter), 'is_available')
    prepopulated_fields = {'slug': ('title',)}
    sortable_by = ('title', 'created_ate', 'price')
    search_fields = ('title', 'slug')


class LetterAdmin(admin.ModelAdmin):
    list_display = ('email', 'pk')


admin.site.register(Category, CategoryAdmin)

admin.site.register(AllService, AllServiceAdmin)

admin.site.register(Letter, LetterAdmin)
