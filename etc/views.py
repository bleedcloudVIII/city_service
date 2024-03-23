from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from etc.forms import CompanyAddPhone, SpecializationCreate, ServiceCreate, CompanyAddService

from etc.models import Company, Phone, Specialization, Service, User
from accounts.models import Account
from django.db.models import Q

from cityservice import renderers

import json

def create_pdf(request):
    print(request.POST)
    print(request.POST['companies'])
    context = {
        'search': request.POST['search'],
        'specs_choose': request.POST['specs_choose'],
        'services_choose': request.POST['services_choose'],
        'companies': request.POST['companies'],
        'phones': request.POST['phones'],
    }
    response = renderers.render_to_pdf("pdfs/invoice.html", context)
    if response.status_code == 404:
        raise HTTP404("Invoice not found")

    filename = f"CityService.pdf"
    """
    Tell browser to view inline (default)
    """
    content = f"inline; filename={filename}"
    download = request.GET.get("download")
    if download:
        """
        Tells browser to initiate download
        """
        content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response

def companies(request):
    context = {}
    if request.method == 'POST':
        companies = []
        phones = []
        if request.POST['specs_choose'] != '':
            specs = request.POST['specs_choose'].split(',')
            services = []
            for spec in specs:
                specialization = Specialization.objects.get(name=spec)
                service_list = list(Service.objects.filter(specialization=specialization))
                companies.extend(list(Company.objects.filter(specializations=specialization)))
                for item in service_list:
                    services.append(item)
            context['services'] = services
        if request.POST['services_choose'] != '':
            services = request.POST['services_choose'].split(',')
            companies = []
            phones = []
            for service in services:
                s = Service.objects.get(name=service)
                companies.extend(list(Company.objects.filter(services=s)))
        if request.POST['search'] != '':
            search = request.POST['search']
            services = list(Service.objects.filter(name__icontains=search))
            specializations = list(Specialization.objects.filter(name__icontains=search))
            companies.extend(list(Company.objects.filter(name__icontains=search)))
            for service in services:
                companies.extend(list(Company.objects.filter(services=service)))
            for spec in specializations:
                companies.extend(list(Company.objects.filter(specializations=spec)))
        companies = set(companies)
        for elem in companies:
            phones.append(list(Phone.objects.filter(company=elem)))
        context['companies'] = companies
        
        context['phones'] = phones
        context['search'] = request.POST['search']
        context['specs_choose'] = request.POST['specs_choose']
        context['services_choose'] = request.POST['services_choose']
    else:
        qs_companies = Company.objects.all()
        
        comps = list(qs_companies)
        phones = []
        qs_phones = {}
        for comp in comps:
            
            phones.append(list(Phone.objects.filter(company=comp)))
        json_companies = {}    
        for i in range(len(qs_companies)):
            json_companies[i] = serializers.serialize('json', [qs_companies[i], ])
        print(str(json_companies))
        w = serializers.serialize('json', qs_companies)
        # print(str(comps[0]))
        # str_companies = "".join(str(elem) for elem in comps)
        # json_companies = {serializers.serialize('json', [elem, ]) for elem in qs_companies}
        # print(json.dumps(qs_companies))
        # print(json.dumps(json_companies))
        # json_phones = {}
        # print(json_companies)
        # print(w)
        # json_companies = serializers.serialize('json', [c, ])
        # print(json_companies)
        # context['str_companies'] = str_companies
        context['json_companies'] = json_companies
        context['phones'] = phones
        context['companies'] = comps
        
        # context['str_companies'] = comps
        
        context['specs_choose'] = ''
        context['services_choose'] = ''
        context['search'] = ''
    context['specs'] = Specialization.objects.all()
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

def company_add_service(request):
    form = CompanyAddService(request.POST)
    if form.is_valid():
        name = request.POST['name']
        service = Service.objects.get(name=name)
        account = Account.objects.get(username=request.user)
        company = Company.objects.get(account=account.pk)
        company.specializations.add(service.specialization)
        company.services.add(service)
    return HttpResponseRedirect(reverse('account_profile'))

def company_delete_service(request):
    account = Account.objects.get(username=request.user)
    company = Company.objects.get(account=account.pk)
    pk = request.POST['pk']
    service = Service.objects.get(id=pk)
    
    count = len(list(company.services.filter(specialization=service.specialization)))
    
    if count == 1:
        company.specializations.remove(service.specialization)
            
    company.services.remove(service)
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

# def change_email(request):
#     print("ASDDQW")
#     print(request.POST)
#     email = request.POST['email']
#     account = Account.objects.get(username=request.user)
#     account.email = email
#     account.save()
#     return HttpResponseRedirect(reverse('account_profile'))

def change_first_name(request):
    first_name = request.POST['first_name']
    account = Account.objects.get(username=request.user)
    user = User.objects.get(account=account.pk)
    user.first_name=first_name
    user.save()
    return HttpResponseRedirect(reverse('account_profile'))

def change_last_name(request):
    last_name = request.POST['last_name']
    account = Account.objects.get(username=request.user)
    user = User.objects.get(account=account.pk)
    user.last_name=last_name
    user.save()
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

def get_service(request):
    print(request.POST)
    context = {}
    return render(request, 'companies.html', context)