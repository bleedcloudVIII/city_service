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

urlpatterns = [
    path('cityservice/admin/', admin.site.urls),
    
    path('cityservice/accounts/registration', registration, name='account_registration'),
    path('cityservice/accounts/login', login, name='account_login'),
    path('cityservice/accounts/logout', logout, name='account_logout'),
    path('cityservice/accounts/profile', profile, name='account_profile'),
    
    path('cityservice/account/add_phone', company_add_phone, name='add_phone'),
    path('cityservice/account/delete_phone', company_delete_phone, name='delete_phone'),
    
    
    path('cityservice/companies', companies, name='companies'),     
]
