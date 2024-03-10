from django.contrib.auth.forms import forms

from etc.models import Company, Specialization, Service

class CompanyAddPhone(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': '+X (XXX) XXX-XX-XX',
            'pattern': '\+[0-9]{1} \([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}',
            'type': 'text',
            'maxlength': 18,
        }
    ))
    
    class Meta:
        model = Company
        fields = ('phone')

class CompanyAddService(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            # 'placeholder': '+X (XXX) XXX-XX-XX',
            # 'pattern': '\+[0-9]{1} \([0-9]{3}\) [0-9]{3}-[0-9]{2}-[0-9]{2}',
            # 'type': 'text',
            # 'maxlength': 18,
        }
    ))
    
    class Meta:
        model = Company
        fields = ('name')

# class CompanyChangeRank(forms.Form):
#     rank = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'cs-input',
#             'placeholder': 'Изменить разряд',
#         }
#     ))
        
#     class Meta:
#         model = Company
#         fields = ('rank')
        
class SpecializationCreate(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите название специализации'
        }
    ))
    
    class Meta:
        model = Specialization
        fields = ('name')
        
        
class ServiceCreate(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите название услуги',
            'onclick': 'select_spec()',
        }
    ))
    
    spec_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите название специализации'
        }
    ))
    
    class Meta:
        model = Service
        fields = ('name')