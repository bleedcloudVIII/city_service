from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from etc.forms import CompanyAddPhone, SpecializationCreate, ServiceCreate

from etc.models import Company, Phone, Specialization, Service
from accounts.models import Account

def companies(request):
    context = {
        # 'companies': Company.objects.all(),
        'companies': Company.objects.all()[:10],
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
    return render(request, 'companies.html', context)

def company_add_phone(request):
    form = CompanyAddPhone(request.POST)
    if form.is_valid():
        phone = request.POST['phone']
        account = Account.objects.get(username=request.user)
        company = Company.objects.get(account=account.pk)
        phone = Phone.objects.create(phone=phone, company=company)
    return HttpResponseRedirect(reverse('account_profile'))

def company_delete_phone(request):
    pk = request.POST['pk']
    phone = Phone.objects.get(id=pk)
    phone.delete()
    return HttpResponseRedirect(reverse('account_profile'))

def change_rank(request):
    rank = request.POST['rank']
    account = Account.objects.get(username=request.user)
    company = Company.objects.get(account=account.pk)
    company.rank = rank
    company.save()
    return HttpResponseRedirect(reverse('account_profile'))

def change_name(request):
    print(request.POST)
    name = request.POST['name']
    account = Account.objects.get(username=request.user)
    company = Company.objects.get(account=account.pk)
    company.name = name
    company.save()
    return HttpResponseRedirect(reverse('account_profile'))

def change_email(request):
    print(request.POST)
    email = request.POST['email']
    account = Account.objects.get(username=request.user)
    company = Company.objects.get(account=account.pk)
    company.email = email
    company.save()
    return HttpResponseRedirect(reverse('account_profile'))

def change_ownership(request):
    type_of_ownership = request.POST['type_of_ownership']
    account = Account.objects.get(username=request.user)
    company = Company.objects.get(account=account.pk)
    company.type_of_ownership = type_of_ownership
    company.save()
    return HttpResponseRedirect(reverse('account_profile'))

def change_address(request):
    print(request.POST)
    address = request.POST['address']
    account = Account.objects.get(username=request.user)
    company = Company.objects.get(account=account.pk)
    company.address = address
    company.save()
    return HttpResponseRedirect(reverse('account_profile'))

def spec_create(request):
    print(request.POST)
    if request.method == 'POST':
        form = SpecializationCreate(request.POST)
        if form.is_valid():
            name = request.POST['name']
            Specialization.objects.create(name=name)
    else:
        form = SpecializationCreate()
    context = {'form': form}
    return render(request, 'specialization.html', context)

def service_create(request):
    print(request.POST)
    if request.method == 'POST':
        form = ServiceCreate(request.POST)
        if form.is_valid():
            name = request.POST['name']
            spec_name = request.POST['spec_name']
            spec = Specialization.objects.get(name=spec_name)
            Service.objects.create(
                name=name,
                specialization=spec
            )
    else:
        form = ServiceCreate()
    specializations = Specialization.objects.all()
    context = {'form': form, 'specs': specializations}
    return render(request, 'service.html', context)