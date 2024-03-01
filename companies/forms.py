from django.contrib.auth.forms import AuthenticationForm, forms

from companies.models import Company

class CompanyLoginForm(AuthenticationForm):
    login = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите логин компании',
            
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите пароль',
            
        }
    ))
    
    class Meta:
        model = Company
        fields = ('login', 'password')
