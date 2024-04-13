from django.db import models
from django.conf import settings
from django_jalali.db import models as jmodels
from django.core.validators import MaxValueValidator, MinValueValidator


User = settings.AUTH_USER_MODEL


class Post(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title          = models.CharField(max_length=100, verbose_name='سربرگ')
    txt            = models.TextField(verbose_name='دیدگاه')
    admin_approval = models.BooleanField(default=False, verbose_name='تایید مدیر')
    vote           = models.PositiveSmallIntegerField(verbose_name='امتیاز', null=False, blank=False,
                                            validators=[MinValueValidator(1),MaxValueValidator(10)])
    created_at     = jmodels.jDateTimeField(auto_now_add=True, verbose_name='نوشته شده در تاریخ')
    
    def __str__(self) -> str:
        return f"{self.user} {self.title} {self.admin_approval} {self.vote}"
    
    class Meta:
        ordering = ['-created_at']
