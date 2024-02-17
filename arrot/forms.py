from django import forms 
from django.core.exceptions import ValidationError

from django_jalali import forms as jforms
from django_jalali.forms.widgets import jDateInput

from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

from .models import ArrotModel, GolsaModel
from .enums import *


################################# Clinic forms #################################


class ClinicReserve(forms.ModelForm):
    class Meta:
        model = ArrotModel
        fields = ("title", "date", "jtime", "hour", "description")
        widgets = {
            'title': forms.Select(attrs={'class':'form-control my-5'}),
            'jtime': jDateInput(attrs={'class': 'form-control my-5', 'placeholder':'1403-11-11'}),
            'hour': forms.Select(attrs={'class':'form-control my-5'}),
            'description': forms.Textarea(attrs={'class':'form-control my-5'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ClinicReserve, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label='روز', widget=AdminJalaliDateWidget)
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        hour = cleaned_data.get('hour')
        title = cleaned_data.get('title')
        if date and hour and title:
            existing_turn = ArrotModel.objects.filter(title=title, date=date, hour=hour).exists()
            if existing_turn:
                raise ValidationError('این نوبت رزرو شده است')
        return cleaned_data


class RepairClinic(forms.Form):
    title       = forms.ChoiceField(choices=ARROT_SERVICES, label="عنوان", widget=forms.Select(attrs={'class':'form-control my-5'}))
    date        = forms.DateField()
    jtime       = jforms.jDateField(label="تاریخ", widget=jforms.jDateInput(attrs={'class':'form-control my-5'}))
    hour        = forms.ChoiceField(choices=HOURS, label="ساعت", widget=forms.Select(attrs={'class':'form-control my-5'}))
    description = forms.CharField(max_length=500, label="توضیحات", widget=forms.Textarea(attrs={'class':'form-control my-5'}))

    def __init__(self, *args, **kwargs):
        super(RepairClinic, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label='تاریخ', widget=AdminJalaliDateWidget)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        hour = cleaned_data.get('hour')
        title = cleaned_data.get('title')
        if date and hour and title:
            existing_turn = ArrotModel.objects.filter(title=title, date=date, hour=hour).exists()
            if existing_turn:
                raise ValidationError('این نوبت رزرو شده است')
        return cleaned_data


################################# Salon forms #################################


class SalonReserve(forms.ModelForm):
    class Meta:
        model = GolsaModel
        fields = ("title", "date", "jtime", "hour", "description")
        widgets = {
            'title': forms.Select(attrs={'class':'form-control my-5'}),
            'jtime': jDateInput(attrs={'class': 'form-control my-5'}),
            'hour': forms.Select(attrs={'class':'form-control my-5'}),
            'description': forms.Textarea(attrs={'class':'form-control my-5'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(SalonReserve, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label='تاریخ', widget=AdminJalaliDateWidget)
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        hour = cleaned_data.get('hour')
        title = cleaned_data.get('title')
        if date and hour and title:
            existing_turn = GolsaModel.objects.filter(title=title, date=date, hour=hour).exists()
            if existing_turn:
                raise ValidationError('این نوبت رزرو شده است')
        return cleaned_data


class RepairSalon(forms.Form):
    title       = forms.ChoiceField(choices=GOLSA_SERVICES, label="عنوان", widget=forms.Select(attrs={'class':'form-control my-5'}))
    date        = forms.DateField()
    jtime       = jforms.jDateField()
    hour        = forms.ChoiceField(choices=HOURS)
    description = forms.CharField(max_length=500)

    def __init__(self, *args, **kwargs):
        super(RepairSalon, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label='روز', widget=AdminJalaliDateWidget)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        hour = cleaned_data.get('hour')
        title = cleaned_data.get('title')
        if date and hour and title:
            existing_turn = GolsaModel.objects.filter(title=title, date=date, hour=hour).exists()
            if existing_turn:
                raise ValidationError('این نوبت رزرو شده است')
        return cleaned_data
