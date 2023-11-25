from django.db import models
from django_jalali.db import models as jmodels
from django.core.validators import RegexValidator


class Category(models.Model):
    title          = models.CharField(max_length=50, verbose_name='عنوان', help_text='عنوان')
    slug           = models.SlugField(max_length=50, unique=True, allow_unicode=True, verbose_name='اسلاگ', help_text='اسلاگ')
    created_at     = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده', help_text='ایجاد شده')
    description    = models.TextField(verbose_name='توضیحات اضافی', help_text='توضیحات اضافی')
    category_cover = models.ImageField(upload_to='category/pic/', null=True, blank=True, verbose_name='تصویر')
    alt_cover      = models.ImageField(upload_to='category/alt/', null=True, blank=True, verbose_name='جایگزین تصویر')
    
    def __str__(self) -> str:
        return f"{self.title} {self.slug}"
    
    class Meta:
        ordering = ['-created_at']


class AllService(models.Model):
    numbers       = RegexValidator(r'^[0-9a]*$', message='Only numbers are allowed.')
    category      = models.ForeignKey(Category, on_delete=models.CASCADE)
    title         = models.CharField(max_length=50, verbose_name='عنوان', help_text='عنوان')
    slug          = models.SlugField(max_length=50, unique=True, allow_unicode=True, verbose_name='اسلاگ', help_text='اسلاگ')
    created_at    = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده', help_text='ایجاد شده')
    description   = models.TextField(verbose_name='توضیحات اضافی', help_text='توضیحات اضافی')
    price         = models.CharField(max_length=12, validators=[numbers], verbose_name='هزینه', help_text='هزینه')
    service_cover = models.ImageField(upload_to='service/pic/', null=True, blank=True, verbose_name='تصویر')
    alt_cover     = models.ImageField(upload_to='service/alt/', null=True, blank=True, verbose_name='جایگزین تصویر')
    
    def __str__(self) -> str:
        return f"{self.category} {self.title}"
    
    class Meta:
        ordering = ['-created_at']


class Letter(models.Model):
    email = models.EmailField(max_length=256, verbose_name='پست الکترونیکی')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    
    def __str__(self) -> str:
        return f"{self.email}"
    
    class Meta:
        ordering = ['-created_at']


class Gallery(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(unique=True, verbose_name='اسلاگ', allow_unicode=True, max_length=50)
    pic = models.ImageField(upload_to='gallery/pic/', verbose_name='تصویر')
    alt_pic = models.ImageField(upload_to='gallery/alt/', verbose_name='جایگزین تصویر')
    
    def __str__(self) -> str:
        return f"{self.title} {self.slug}"
