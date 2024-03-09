from django.contrib.auth.forms import forms

from etc.models import Company

class CompanyAddPhone(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': '+X (XXX) XXX-XX-XX',
            'pattern': '\+[0-9]{1} \([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}',
            # 'pattern': '\+?[0-9\s\-\(\)]+',
            
            # 'pattern': '[0-9]{1} [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}',
            'type': 'text',
            'maxlength': 18,
        }
    ))
    
    class Meta:
        model = Company
        fields = ('phone')

class CompanyChangeRank(forms.Form):
    rank = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Изменить разряд',
        }
    ))
        
    class Meta:
        model = Company
        fields = ('rank')