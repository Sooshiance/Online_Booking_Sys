from django.db import models
from django.conf import settings
from django_jalali.db import models as jmodels


User = settings.AUTH_USER_MODEL


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=256, verbose_name='پرسش')
    txt = models.TextField(verbose_name='متن پرسش')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان نگارش')
    
    def __str__(self) -> str:
        return f"{self.user} {self.title}"
    
    class Meta:
        ordering = ['-created_at']


class RepetitiveQuestion(models.Model):
    title = models.CharField(max_length=256, verbose_name='پرسش')
    txt = models.TextField(verbose_name='پاسخ')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان نگارش')
    updated_at = jmodels.jDateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        ordering = ['-created_at']
