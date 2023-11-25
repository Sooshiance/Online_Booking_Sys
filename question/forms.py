from django import forms 

from .models import Question


class Ask(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'txt']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control my-5','placeholder':'عنوان'}),
            'txt':forms.Textarea(attrs={'class':'form-control my-5','placeholder':'متن پرسش را درج کنید'}),
        }
