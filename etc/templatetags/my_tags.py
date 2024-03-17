from django import template

from etc.models import Company, Phone, Specialization, Service, User
from accounts.models import Account

register = template.Library()

@register.simple_tag()
def get_services(specs):
    # print('SADa')
    # print(context)
    # specs = context['specs_choose']
    print(specs)
    services = []
    if specs != '':
        specs = specs.split(',')
        for spec in specs:
            try:
                specialization = Specialization.objects.get(name=spec)
                l = list(Service.objects.filter(specialization=specialization))
                for item in l:
                    services.append(item)
            except:
                print('Error')
    print(services)
    # context['services'] = services 
    return {'services': services}