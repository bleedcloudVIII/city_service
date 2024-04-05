from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from accounts.forms import AccountRegistrationForm, AccountLoginForm
from etc.forms import CompanyAddPhone, CompanyAddService

from accounts.models import Account, Group

from etc.models import User, Company, Phone, Specialization, Service

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
            print(company)
            # spec = Specialization.objects.get(id=1)
            # service = Service.objects.get(id=1)
            # company.specializations.add(spec)
            # company.services.add(service)
            print(company.services.all())
            context['allServices'] = Service.objects.all()
            context['info'] = company
            context['formPhone'] = CompanyAddPhone()
            context['formService'] = CompanyAddService()
            context['phones'] = phones
            context['services'] = company.services.all()
    else:
            # Return Error
        pass
    return render(request, 'profile.html', context)

def registration(request):
    if request.method == 'POST':
        form = AccountRegistrationForm(data=request.POST)
        email = request.POST['email']
        is_email_used = Account.objects.filter(email=email)
        print(email)
        print(is_email_used)
        if is_email_used.count() != 0:
            form.add_error('email', 'Этот email уже занят')
        if form.is_valid():
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            group = request.POST['choice']
            email = request.POST['email']
            if group == 'user':
                print("QWEQWEQWEQWE")
                account = Account.objects.create_user(
                    username=username,
                    password=password1,
                    group_id=1,
                    email=email,
                )
                user = User.objects.create(
                    account=account,
                )
            else:
                account = Account.objects.create_user(
                    username=username,
                    password=password1,
                    group_id=2,
                    email=email,
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