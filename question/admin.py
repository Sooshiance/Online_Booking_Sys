from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter

from .models import Question, RepetitiveQuestion


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'pk')
    list_filter = (('created_at', JDateFieldListFilter),)
    readonly_fields = ('created_at',)
    search_fields = ('user', 'title')
    list_display_links = ('user', 'title')


class RepetitveAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = (('created_at', JDateFieldListFilter),
                    ('updated_at', JDateFieldListFilter))


admin.site.register(Question, QuestionAdmin)

admin.site.register(RepetitiveQuestion, RepetitveAdmin)
