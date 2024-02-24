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


class Phone(models.Model):
    phone = models.CharField(max_length=15) # ????

    # company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "phone"


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True) # on_delete = ...
    name = models.CharField(max_length=150)
    rank = models.IntegerField()
    type_of_ownership = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phones = models.ForeignKey(Phone, on_delete=models.SET_NULL, null=True) # on_delete = ...
    # holidays = models.ForeignKey(Day_of_work) # ????
    # orders = models.ForeignKey(Order)
    # service = models.ForeignKey(Service)
    
    class Meta:
        db_table = "company"

class Service(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    # companies = models.ForeignKey(Company, on_delete=models.SET_NULL)
    
    class Meta:
        db_table = "service"

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


class Service_Company(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    company = models.OneToOneField(Company, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = "service_company"

class Order_User(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = "order_user"


        

