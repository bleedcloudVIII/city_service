from django.contrib.auth.forms import AuthenticationForm

from companies.models import Company

class CompanyLoginForm(AuthenticationForm):
    class Meta:
        model = Company
        fields = ('name', 'nickname', 'password')