from django import forms 

from .models import Letter


class Paper(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['email']
