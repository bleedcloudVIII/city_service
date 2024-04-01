from django.contrib import admin

from etc.models import User, Company, Specialization, Service
from accounts.models import  Account

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["pk", "account", "first_name", "last_name"]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["pk", "account", "name", "address"]
    
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["pk", "username", "email", "password", "is_staff", "is_superuser"]
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "specialization"]

