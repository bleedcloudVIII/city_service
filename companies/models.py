from django.db import models
# from cityservice import User
# from users import User
# from users.models import User

class Service(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    
    class Meta:
        db_table = "service"

class Specialization(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    
    services = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "specialization"

class Holiday(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    comment = models.CharField(max_length=150)
    
    class Meta:
        db_table = "holiday"

class Day_of_work(models.Model):
    time_open = models.TimeField()
    time_close = models.TimeField()
    day_of_start_week = models.DateField()
    weekday = models.IntegerField()
    
    class Meta:
        db_table = "day_of_work"

class Phone(models.Model):
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = "phone"

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    is_active = models.BooleanField()
    
    service = models.OneToOneField(Service, on_delete=models.CASCADE)

    
    class Meta:
        db_table = "order"

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=150, null=False)
    name = models.CharField(max_length=150, null=False) #blank = False?
    rank = models.IntegerField()
    type_of_ownership = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    
    services = models.ManyToManyField(Service)
    specializations = models.ManyToManyField(Specialization)
    holidays = models.ManyToManyField(Holiday)
    day_of_work = models.ManyToManyField(Day_of_work)
    
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    phones = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "company"
