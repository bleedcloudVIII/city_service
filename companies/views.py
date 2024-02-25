from django.shortcuts import render, HttpResponse

from companies.models import Company


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
    return render(request, 'company_login.html')

def profile(request):
    return render(request, 'company_profile.html')