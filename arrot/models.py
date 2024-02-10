from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django_jalali.db import models as jmodels

from .utils import passedDays, noFriday


User = settings.AUTH_USER_MODEL
Max_Limit = settings.MAX_LIMIT


ARROT_SERVICES = (
    ('هایفو تراپی', 'هایفو تراپی'),
    ('فشیال پاکسازی پوست', 'فشیال پاکسازی پوست'),
    ('تزریق بوتاکس', 'تزریق بوتاکس'),
    ('تزریق فیلر', 'تزریق فیلر'),
    ('تزریق ژل', 'تزریق ژل'),
    ('لیزر مو های زائد', 'لیزر مو های زائد'),
    ('مزو تراپی', 'مزو تراپی'),
    ('لاغری با دستگاه', 'لاغری با دستگاه'),
    ('مشاوره تغذیه', 'مشاوره تغذیه'),
    ('میکرونیدلینگ', 'میکرونیدلینگ'),
)


GOLSA_SERVICES = (
    ('کاشت مژه', 'کاشت مژه'),
    ('کاشت ناخن', 'کاشت ناخن'),
    ('هایلایت ابرو', 'هایلایت ابرو'),
)


HOURS = (
    ('08-10', '08-10'),
    ('10-12', '10-12'),
    ('12-14', '12-14'),
    ('14-16', '14-16'),
    ('16-18', '16-18'),
)


class ArrotModel(models.Model):
    objects        = jmodels.jManager()
    user           = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title          = models.TextField(choices=ARROT_SERVICES, verbose_name='نام خدمات')
    hour           = models.CharField(max_length=5, choices=HOURS, verbose_name='زمان انتخابی')
    date           = jmodels.jDateField(validators=[passedDays, noFriday], verbose_name='روز انتخابی')
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
    date           = jmodels.jDateField(validators=[passedDays, noFriday], verbose_name='روز انتخابی')
    description    = models.TextField(null=True, blank=True, verbose_name='توضیح کوتاه')
    admin_approval = models.BooleanField(default=False, verbose_name='تایید مدیر')
    created_at     = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    updated_at     = jmodels.jDateTimeField(auto_now=True, verbose_name='به روز شده در')
    
    def __str__(self) -> str:
        return f"{self.user} : {self.title} in {self.hour} {self.admin_approval}"
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['title', 'hour', 'date']


class Wallet(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    reach_limit = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(Max_Limit)], default=1)    

    def __str__(self) -> str:
        return f"{self.user} {self.reach_limit}"
