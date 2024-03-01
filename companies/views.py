from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from companies.models import Company

from companies.forms import CompanyLoginForm

# Ремонт
# Пошив
# Техническое обслуживание
# Прачечная                           
# Фотоателье
# Баня
# Парикмахерская
# Ритуальные услуги

def index(request):
    # Пока не выбраны услуги и т.д.
    # То берутся первые 10 компаний
    
    companies = [
        {
          'name': 'ADdas',
          'spez': 'adqwadda',
        },
        {
          'name': 'ADdas',
          'spez': 'adqwadda',
        },
        {
          'name': 'ADdas',
          'spez': 'adqwadda',
        },
        {
          'name': 'ADdas',
          'spez': 'adqwadda',
        },
        {
          'name': 'ADdas',
          'spez': 'adqwadda',
        },
        {
          'name': 'ADdas',
          'spez': 'adqwadda',
        },
        {
          'name': 'ADdas',
          'spez': 'adqwadda',
        },
        {
          'name': 'ADdas',
          'spez': 'adqwadda',
        },
        {
          'name': 'ADdas',
          'spez': 'adqwadda',
        },
    ]
    
    context = {
        # 'companies': Company.objects.all(),
        'companies': companies[0:5],
        'spezs': [
            {
                'name': 'Ремонт',
            },
            {
                'name': 'Пошив',
            },
            {
                'name': 'Техническое обслуживание',
            },
            {
                'name': 'Прачечная',
            },
            {
                'name': 'Фотоателье',
            },
            {
                'name': 'Баня',
            },
            {
                'name': 'Парикмахерчкая',
            },
            {
                'name': 'Ритуальные услуги',
            },
        ],
        'services': [
            {
                'name': 'Ремонт часов',
            },
            {
                'name': 'Ремонт мебели',
            },
        ],
    }

    return render(request, 'company_index.html', context)

def registration(request):
   	return render(request, 'company_registration.html')

def login(request):
    if request.method == 'POST':
        form = CompanyLoginForm(data=request.POST)
        print(form.errors)
        print('Valid')
        print(form.is_valid())
        if form.is_valid():
            login = request.POST['login']
            password = request.POST['password']
            company = auth.authenticate(login=login, password=password)
            if True:
                print("asd")
                auth.login(request, user)
                return HttpResponseRedirect(reverse('cityservice'))
    else:
        form = CompanyLoginForm()
    context = {
		'form': form
	}
    return render(request, 'company_login.html', context)


def profile(request):
   	return render(request, 'company_profile.html')