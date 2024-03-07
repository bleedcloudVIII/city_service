# from django.db import models

# from accounts.models import Account
# from users.models import User

# class Specialization(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150, null=False)
    
#     # services = models.ForeignKey(Service, on_delete=models.CASCADE)
    
#     class Meta:
#         db_table = "specialization"

# class Service(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150, null=False)
    
#     specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    
#     class Meta:
#         db_table = "service"


# class Holiday(models.Model):
#     id = models.IntegerField(primary_key=True)
#     date = models.DateField()
#     comment = models.CharField(max_length=150)
    
#     class Meta:
#         db_table = "holiday"

# class Day_of_work(models.Model):
#     id = models.IntegerField(primary_key=True)
#     time_open = models.TimeField()
#     time_close = models.TimeField()
#     day_of_start_week = models.DateField()
#     weekday = models.IntegerField()
    
#     class Meta:
#         db_table = "day_of_work"


# class Company(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150, null=False) #blank = False?
#     rank = models.IntegerField(null=True)
#     type_of_ownership = models.CharField(max_length=150, null=True)
#     address = models.CharField(max_length=200, null=True)
    
#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
#     services = models.ManyToManyField(Service)
#     specializations = models.ManyToManyField(Specialization)
#     holidays = models.ManyToManyField(Holiday)
#     day_of_work = models.ManyToManyField(Day_of_work)
    
#     # orders = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
#     # phones = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True)

#     class Meta:
#         db_table = "company"
        
# class Phone(models.Model):
#     id = models.IntegerField(primary_key=True)
#     phone = models.CharField(max_length=15, null=False)

#     company = models.ForeignKey(Company, on_delete=models.CASCADE)

#     class Meta:
#         db_table = "phone"
        
# class Order(models.Model):
#     id = models.IntegerField(primary_key=True)
#     is_active = models.BooleanField()
    
#     services = models.ManyToManyField(Service)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     class Meta:
#         db_table = "order"
