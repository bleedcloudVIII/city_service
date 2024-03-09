from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms,  UserCreationForm

from accounts.models import Account
from etc.models import Company

class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите username',
        }
    ))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите пароль',
            
        }
    ))
    
    class Meta:
        model = Account
        fields = ('username', 'password')
        
class AccountRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите username',
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
    
    choice = forms.ChoiceField(choices=[('user', 'Пользователь'), ('company', 'Компания')])
    
    class Meta:
      model = Account
      fields = ('username', 'password1', 'password2', 'choice') 
