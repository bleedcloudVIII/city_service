from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from etc.forms import CompanyAddPhone, SpecializationCreate, ServiceCreate, CompanyAddService
from django.template.loader import get_template
from etc.models import Company, Phone, Specialization, Service, User, Review
from accounts.models import Account
from django.db.models import Q
from cityservice import settings
from cityservice import renderers
from xhtml2pdf import pisa
from xhtml2pdf.files import pisaFileObject
import os
import json
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime

def add_view(request):
    print(request.POST)
    company = Company.objects.get(id = request.POST['company_pk'])
    
    account = Account.objects.get(username=request.user)
    if (account.group.id == 1):
        user = User.objects.get(account=account.pk)        
        Review.objects.create(company=company, user=user, text=request.POST['view'], date=datetime.datetime.now())
        
    phones = Phone.objects.filter(company=company)
    views = Review.objects.filter(company=company)
    # accounts = []
    # for view in views:
    #     accounts.extend(Account.objects.get(id=view.user.account))
    context = {
        'company': company,
        'phones': phones,
        'views': views,
        # 'accounts': accounts,
    }
    return render(request, 'company.html', context)

def get_company(request):
    company = Company.objects.get(id = request.POST['pk'])
    phones = Phone.objects.filter(company=company)
    views = Review.objects.filter(company=company)
    # accounts = []
    # for view in views:
    #     accounts.append(Account.objects.get(id=view.user.account.pk))
    
    context = {
        'company': company,
        'phones': phones,
        'views': views,
        # 'accounts': accounts,
    }
    
    return render(request, 'company.html', context)

def get_list(list_phones):
    phones = list_phones
    
    phones = phones.replace("[", "")
    phones = phones.replace("]", "/")
    phones = phones.replace(",", "")
    phones = phones.replace("//", "")
    phones = phones.replace("'", "")

    phones = phones.split("/")
    phones = [phone.replace("+", "#+") for phone in phones]
    phones = [phone.split("#") for phone in phones]
    phones = [[ phone for phone in l if len(phone) >= 18] for l in phones]
    return phones

def fetch_pdf_resources(uri, rel):
    # if uri.find(settings.MEDIA_URL) != -1:
    #     path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    if uri.find(settings.STATIC_URL) != -1:
        path = os.path.join('static/', uri.replace(settings.STATIC_URL, ''))
    else:
        path = None
    return path

def create_pdf(request):
    template_path = 'pdfs/invoice.html'
    phones = []
    companies = []
    
    if request.POST['companies'] != '':
        companies = json.loads(request.POST['companies'].replace("'", "\""))
    
    if request.POST['phones'] != '':
        phones = get_list(request.POST['phones'])
    
    print(request.POST['phones'])
    
    context = {
        "companies": companies,
        "phones": phones,
    }
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisaFileObject.getNamedFile = lambda self: self.uri
    pisa_status = pisa.CreatePDF(html, dest=response, encoding='UTF-8', link_callback=fetch_pdf_resources)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
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
            print(search)
            print(type(search))
            # Запрос с ИЛИ где 3 значения, нижний регистр, верхний регистр и верхний регист у 1-го символа
            services = list(Service.objects.filter(Q(name__icontains=search) | Q(name__icontains=search.upper()) | Q(name__icontains=search.lower()) | Q(name__icontains=search.lower().title())))
            specializations = list(Specialization.objects.filter(Q(name__icontains=search) | Q(name__icontains=search.upper()) | Q(name__icontains=search.lower()) | Q(name__icontains=search.lower().title())))
            companies.extend(list(Company.objects.filter(Q(name__icontains=search) | Q(name__icontains=search.upper()) | Q(name__icontains=search.lower()) | Q(name__icontains=search.lower().title()))))
            for service in services:
                companies.extend(list(Company.objects.filter(services=service)))
            for spec in specializations:
                companies.extend(list(Company.objects.filter(specializations=spec)))
        companies = set(companies)
        for elem in companies:
            phones.append(list(Phone.objects.filter(company=elem)))
        
        pdf_companies = [{'pk': company.pk, 'name': company.name, 'address': company.address} for company in companies]
        pdf_phones = [[p.phone for p in phone] for phone in phones]
        
        context['companies'] = companies
        context['pdf_companies'] = pdf_companies
        context['pdf_phones'] = pdf_phones
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
            
        pdf_companies = [{'pk': company.pk, 'name': company.name, 'address': company.address} for company in qs_companies]
        pdf_phones = [[p.phone for p in phone] for phone in phones]
        
        context['pdf_companies'] = pdf_companies
        context['pdf_phones'] = pdf_phones
        context['phones'] = phones
        context['companies'] = comps
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

def change_description(request):
    print(request.POST)
    description = request.POST['description']
    account = Account.objects.get(username=request.user)
    company = Company.objects.get(account=account.pk)
    company.description = description
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