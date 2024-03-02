from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms,  UserCreationForm

from companies.models import Company

class CompanyLoginForm(forms.Form):
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
        fields = ('username', 'password')
        
class CompanyRegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите название компании',
        }
    ))
    
    login = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите логин компании',
        }
    ))
    
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите пароль',
        }
    ))
    
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Повторите пароль',
        }
    ))
    class Meta:
      model = Company
      fields = ('name', 'login', 'password1', 'password2') 
