from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms,  UserCreationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите имя пользователя',
        }
    ))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите пароль',
            
        }
    ))
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите имя пользователь',
        }
    ))
    
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите имя',
        }
    ))
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'cs-input',
            'placeholder': 'Введите фамилию',
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
      model = User
      fields = ('first_name', 'last_name', 'username', 'password1', 'password2') 
