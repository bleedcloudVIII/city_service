from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.core.exceptions import ValidationError

from accounts.forms import AccountRegistrationForm, AccountLoginForm

from accounts.models import Account, Group

from etc.models import User, Company
    
def logout(request):
    print(request)
    print(request.user)
    auth.logout(request)
    return HttpResponseRedirect(reverse('companies'))    
    
def registration(request):
    if request.method == 'POST':
        form = AccountRegistrationForm(data=request.POST)
        print(request.POST)
        print(form.errors.as_json())
        if form.is_valid():
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            group = request.POST['choice']
            if group == 'user':
                account = Account.objects.create_user(
                    username=username,
                    password=password1,
                    group_id=1,
                )
                user = User.objects.create(
                    account=account,
                )
            else:
                account = Account.objects.create_user(
                    username=username,
                    password=password1,
                    group_id=2,
                )
                company = Company.objects.create(
                    account=account,
                )
            return HttpResponseRedirect(reverse('account_login'))
    else:
        form = AccountRegistrationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)

def login(request):
    if request.method == 'POST':
        form = AccountLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            account = auth.authenticate(username=username, password=password)
            if account:
                auth.login(request, account)
                return HttpResponseRedirect(reverse('companies'))
    else:
        form = AccountLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def profile(request):
    return render(request, 'profile.html')