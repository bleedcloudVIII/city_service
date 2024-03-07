# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from companies.models import Order

# from accounts.models import Account

# class Role(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150, unique=True)
    
#     class Meta:
#         db_table = "auth_role"  
        
# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)

#     account = models.ForeignKey(Account, on_delete=models.CASCADE)

#     roles = models.ManyToManyField(Role) # Убрать 0
#     # orders = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    
#     class Meta:
#         db_table = "auth_user"
    