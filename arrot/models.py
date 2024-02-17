from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django_jalali.db import models as jmodels

from .enums import *
from .utils import passedDays, noFriday


User = settings.AUTH_USER_MODEL
Max_Limit = settings.MAX_LIMIT


class ArrotModel(models.Model):
    objects        = jmodels.jManager()
    user           = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title          = models.TextField(choices=ARROT_SERVICES, verbose_name='نام خدمات')
    hour           = models.CharField(max_length=5, choices=HOURS, verbose_name='زمان انتخابی')
    date           = models.DateField(validators=[passedDays, noFriday], verbose_name='روز انتخابی')
    jtime          = jmodels.jDateField(validators=[], verbose_name='روز انتخابی', help_text='داده بالا را عینا اینجا وارد کنید', null=True, blank=True)
    description    = models.TextField(null=True, blank=True, verbose_name='توضیحات کوتاه')
    admin_approval = models.BooleanField(default=False, verbose_name='تایید مدیر')
    created_at     = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    updated_at     = jmodels.jDateTimeField(auto_now=True, verbose_name='به روز شده در')
    
    def __str__(self) -> str:
        return f"{self.user} : {self.title} in {self.hour} {self.admin_approval}"
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['title', 'hour', 'date']


class GolsaModel(models.Model):
    objects        = jmodels.jManager()
    user           = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title          = models.TextField(choices=GOLSA_SERVICES, verbose_name='نام خدمات')
    hour           = models.CharField(max_length=5, choices=HOURS, verbose_name='زمان انتخابی')
    date           = models.DateField(validators=[passedDays, noFriday], verbose_name='روز انتخابی')
    jtime          = jmodels.jDateField(validators=[], verbose_name='روز انتخابی', help_text='داده بالا را عینا اینجا وارد کنید')
    description    = models.TextField(null=True, blank=True, verbose_name='توضیح کوتاه')
    admin_approval = models.BooleanField(default=False, verbose_name='تایید مدیر')
    created_at     = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    updated_at     = jmodels.jDateTimeField(auto_now=True, verbose_name='به روز شده در')
    
    def __str__(self) -> str:
        return f"{self.user} : {self.title} in {self.hour} {self.admin_approval}"
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['title', 'jtime', 'hour', 'date']


class Wallet(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name="user_wallet")
    reach_limit = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(Max_Limit)], default=0)
    
    def remove_turn(self):
        self.reach_limit -= 1
        self.save()
    
    def fallbackCounter(self):
        if self.reach_limit == 10:
            self.reach_limit = 0

    def __str__(self) -> str:
        return f"{self.user} {self.reach_limit}"
