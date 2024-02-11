from django import forms 
from django.core.exceptions import ValidationError

from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

from .models import ArrotModel, GolsaModel


class ClinicReserve(forms.ModelForm):
    class Meta:
        model = ArrotModel
        fields = ("title", "date", "hour", "description")
        widgets = {
            'title': forms.Select(attrs={'class':'form-control my-5'}),
            # 'date': forms.DateInput(attrs={'class': 'form-control my-5'}),
            'hour': forms.Select(attrs={'class':'form-control my-5'}),
            'description': forms.Textarea(attrs={'class':'form-control my-5'}),
        }
    def __init__(self, *args, **kwargs):
        super(ClinicReserve, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label='روز', # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
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


class SalonReserve(forms.ModelForm):
    class Meta:
        model = GolsaModel
        fields = ("title", "date", "hour", "description")
        widgets = {
            'title': forms.Select(attrs={'class':'form-control my-5'}),
            # 'date': jDateInput(attrs={'class': 'form-control my-5'}),
            'hour': forms.Select(attrs={'class':'form-control my-5'}),
            'description': forms.Textarea(attrs={'class':'form-control my-5'}),
        }
    def __init__(self, *args, **kwargs):
        super(SalonReserve, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label='روز', # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
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
