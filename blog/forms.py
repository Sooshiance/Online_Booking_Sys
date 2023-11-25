from django.core.exceptions import ValidationError
from django import forms 

from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'txt', 'vote']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-5','placeholder':'عنوان'}),
            'txt': forms.Textarea(attrs={'class':'form-control my-5','placeholder':'توضیحات بیشتر'}),
            'vote': forms.NumberInput(attrs={'class':'form-control my-5', 'placeholder':'یک عدد از 1 تا 10'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        vote = cleaned_data.get('vote')
        if vote > 10 and vote < 1:
            raise ValidationError('تنها مقادیر بین یک و ده پذیرفته میشوند')
        return cleaned_data
