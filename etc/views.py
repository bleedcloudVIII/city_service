from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from etc.forms import CompanyAddPhone, SpecializationCreate, ServiceCreate, CompanyAddService
from django.template.loader import get_template
from etc.models import Company, Phone, Specialization, Service, User
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
def fetch_pdf_resources(uri, rel):
    # if uri.find(settings.MEDIA_URL) != -1:
    #     path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    # if uri.find(settings.STATIC_URL) != -1:
    #     path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
    # else:
    #     path = None
    # return path
    pass

def create_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    # (0; 0) - левый нижний угол

    font = TTFont('MyFont', './times.ttf')
    pdfmetrics.registerFont(font)
    p.setFont('MyFont', 14)
    
    if request.POST['companies'] != '':
        companies = json.loads(request.POST['companies'].replace("'", "\""))
    
    print(companies)
    print(type(companies))
    print(companies[0]['name'])
    
    
    for i in range(len(companies)):
        p.drawString((i+1)* 100, (7 - i)*100, companies[i]['name'])
        p.drawString((i+2)* 100, (7 - i)*100, companies[i]['address'])
        
    
    # context = {
    #     'search': request.POST['search'],
    #     'specs_choose': request.POST['specs_choose'],
    #     'services_choose': request.POST['services_choose'],
    #     'companies': comp,
    #     # 'phones': request.POST['phones'],
    # }

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="CityService.pdf")
    
    # template_path = 'pdfs/invoice.html'
    # comp = request.POST['companies']
    # comp = comp.replace("'", "\"")
    # comp = json.loads(comp)
    # context = {
    #     'search': request.POST['search'],
    #     'specs_choose': request.POST['specs_choose'],
    #     'services_choose': request.POST['services_choose'],
    #     'companies': comp,
    #     # 'phones': request.POST['phones'],
    # }
    # # Create a Django response object, and specify content_type as pdf
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # # find the template and render it.
    # template = get_template(template_path)
    # html = template.render(context)

    # # create a pdf
    # pisaFileObject.getNamedFile = lambda self: self.uri
    # pisa_status = pisa.CreatePDF(html, dest=response, encoding='UTF-8', link_callback=fetch_pdf_resources)
    # # if error then show some funny view
    # if pisa_status.err:
    #    return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response
    
    
    # # print(request.POST)
    # # print(request.POST['companies'])
    # companies_req = request.POST['companies']
    # # IF
    # # companies_list = list(request.POST['companies'])
    # print(companies_req)
    # print(request.POST['phones'])
    # comp = request.POST['companies']
    # comp = comp.replace("'", "\"")
    # comp = json.loads(comp)
    # print(comp[0])
    # print(type(request.POST['companies']))
    # # print(comp)
    # context = {
    #     'search': request.POST['search'],
    #     'specs_choose': request.POST['specs_choose'],
    #     'services_choose': request.POST['services_choose'],
    #     'companies': comp,
    #     # 'phones': request.POST['phones'],
    #     # 'comp': request.POST['companies'][0],
    #     # 'qwe': 'qwerty',
    #     # 'comps': Company.objects.all(),
    # }
    # response = renderers.render_to_pdf("pdfs/invoice.html", context)
    # if response.status_code == 404:
    #     raise HTTP404("Invoice not found")

    # filename = f"CityService.pdf"
    # content = f"inline; filename={filename}"
    
    # download = request.GET.get("download")
    # if download:
    #     content = f"attachment; filename={filename}"
        
    # response["Content-Disposition"] = content
    # return response

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
            
        pdf_companies = [{'pk': company.pk, 'name': company.name, 'address': company.address} for company in qs_companies]
        pdf_phones = [[p.phone for p in phone] for phone in phones]
        
        context['pdf_companies'] = pdf_companies
        context['pdf_phones'] = pdf_phones
        
        print(pdf_companies)
        print(pdf_phones)
        # data = [{'id': blog.pk, 'name': blog.name} for blog in blogs]
        # print()
        # print(context['companies'])
        # json_companies = {}    
        # for i in range(len(qs_companies)):
            # json_companies[i] = serializers.serialize('json', [qs_companies[i], ])
        # print(str(json_companies))
        
        
        
        # context['json_companies'] = json_companies
        context['phones'] = phones
        context['companies'] = comps
        # context['json'] = json.dumps(json_companies)
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