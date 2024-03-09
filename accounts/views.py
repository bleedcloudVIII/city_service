from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from accounts.forms import AccountRegistrationForm, AccountLoginForm
from etc.forms import CompanyAddPhone

from accounts.models import Account, Group

from etc.models import User, Company, Phone

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('companies'))    
    



def profile(request):
    account = Account.objects.get(username=request.user)
    context = {}
    if account:
        context['account'] = account
        if account.group.id == 1:
            # Account is user
            user = User.objects.get(account=account.pk)
            context['info'] = user
        else:
            # Account is company
            company = Company.objects.get(account=account.pk)
            # phones = Phone.objects.get(company=company.pk)
            # print(company.services)
            # print(company.services)
            phones = Phone.objects.filter(company=company.pk)
            print(phones)
            context['info'] = company
            context['formPhone'] = CompanyAddPhone()
            context['phones'] = phones
    else:
            # Return Error
        pass
    return render(request, 'profile.html', context)

def registration(request):
    if request.method == 'POST':
        form = AccountRegistrationForm(data=request.POST)
        print(form.errors.as_data())
        
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
        print(form.errors.as_data())
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