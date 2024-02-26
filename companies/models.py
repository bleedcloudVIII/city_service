from django.db import models
# from cityservice import User
# from users import User
from users.models import User

class Specialization(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    
    # companies = models.
    
    class Meta:
        db_table = "specialization"

class Specialization_Company(models.Model):
    specialization = models.OneToOneField(Specialization, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "specialization_company"




class Phone(models.Model):
    phone = models.CharField(max_length=15) # ????

    # company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "phone"

class Service_Company(models.Model):
    
    class Meta:
        db_table = "service_company"

class Service(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    companies = models.ForeignKey(Service_Company, on_delete=models.CASCADE)
    
    
    # companies = models.ForeignKey(Company, on_delete=models.SET_NULL)
    
    class Meta:
        db_table = "service"

# class Specialization_Service(models.Model):
    
#     class Meta:
#         db_table = "specailization_service"

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=150, null=False, unique=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True) # on_delete = ...
    name = models.CharField(max_length=150)
    rank = models.IntegerField()
    type_of_ownership = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    
    services = models.ManyToManyField(Service)
    phones = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True)
    specializations = models.ForeignKey(Specialization_Company, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "company"



class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    is_active = models.BooleanField()
    
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    service = models.OneToOneField(Service, on_delete=models.PROTECT)
    company = models.OneToOneField(Company, on_delete=models.PROTECT)
    
    class Meta:
        db_table = "order"


class Holiday(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    comment = models.CharField(max_length=150)
    
    companies = models.ManyToManyField(Company) # ????
    
    class Meta:
        db_table = "holiday"


class Day_of_work(models.Model):
    time_open = models.TimeField()
    time_close = models.TimeField()
    day_of_start_week = models.DateField()
    weekday = models.IntegerField()
    
    companies = models.ManyToManyField(Company)
    
    class Meta:
        db_table = "day_of_work"




class Order_User(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = "order_user"


        

