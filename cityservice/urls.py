"""
URL configuration for cityservice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from accounts.views import registration_user
# from accounts.views import registration_company

# from accounts.views import login_user
# from accounts.views import login_company

from accounts.views import registration
from accounts.views import login
from accounts.views import logout
from accounts.views import profile
# from accounts.views import comapny_add_phone

from etc.views import companies
from etc.views import company_add_phone
from etc.views import company_delete_phone
from etc.views import company_add_service
from etc.views import company_delete_service
from etc.views import change_rank
# from etc.views import change_email
from etc.views import change_name
from etc.views import change_description
from etc.views import change_ownership
from etc.views import change_address
from etc.views import spec_create
from etc.views import service_create
from etc.views import change_first_name
from etc.views import change_last_name
from etc.views import get_service
from etc.views import add_view
from etc.views import create_pdf
from etc.views import get_company

urlpatterns = [
    path('cityservice/admin/', admin.site.urls),
    
    path('cityservice/accounts/registration', registration, name='account_registration'),
    path('cityservice/accounts/login', login, name='account_login'),
    path('cityservice/accounts/logout', logout, name='account_logout'),
    path('cityservice/accounts/profile', profile, name='account_profile'),
    
    path('cityservice/account/add_phone', company_add_phone, name='add_phone'),
    path('cityservice/account/delete_phone', company_delete_phone, name='delete_phone'),
    
    path('cityservice/account/change_description', change_description, name='change_description'),
    path('cityservice/account/change_rank', change_rank, name='change_rank'),
    path('cityservice/account/change_name', change_name, name='change_name'),
    path('cityservice/account/change_ownership', change_ownership, name='change_ownership'),
    path('cityservice/account/change_address', change_address, name='change_address'),
    
    path('cityservice/companies/', get_company, name='company'),
    
    path('cityservice/specialization/create', spec_create, name='spec_create'),
    path('cityservice/service/create', service_create, name='service_create'),
    
    path('cityservice/account/change_first_name', change_first_name, name='change_first_name'),
    path('cityservice/account/change_last_name', change_last_name, name='change_last_name'),
    
    path('cityservice/companies/create_pdf', create_pdf, name='create_pdf'),
    path('cityservice/companies/add_view', add_view, name='add_view'),
    
    
    path('cityservice/account/add_service', company_add_service, name='add_service'),
    path('cityservice/account/delete_service', company_delete_service, name='delete_service'),
    
    path('cityservice/companies', companies, name='companies'),     
]
