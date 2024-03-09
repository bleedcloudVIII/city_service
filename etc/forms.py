from django.contrib.auth.forms import forms

from etc.models import Company

class CompanyAddPhone(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Добавить телефон',
        }
    ))
    
    class Meta:
        model = Company
        fields = ('phone')