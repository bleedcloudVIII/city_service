from django.shortcuts import render, HttpResponse

def index(request):
    # Пока не выбраны услуги и т.д.
    # То берутся первые 10 компаний
    context = {
        'companies':[
            {'name': 'Company1',
                'spez': 'Parikmaxerskaya',
                'services': [
                'strizka', 'okrashivanie',
            ]},
            {'name': 'Company2',
                'spez': 'Banya',
                'services': [
                'Banya', 'Sauna', 'Hamam',
            ]},
        ]
    }
    return render(request, 'company_index.html', context)

def registration(request):
    return render(request, 'company_registration.html')

def login(request):
    return render(request, 'company_login.html')

def profile(request):
    return render(request, 'company_profile.html')