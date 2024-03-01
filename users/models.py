from django.db import models
from django.contrib.auth.models import AbstractUser
from companies.models import Order

class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    
    class Meta:
        db_table = "auth_role"  
        
# Создаю свою модель вместо стандартной!!!!
class User(AbstractUser):
    roles = models.ManyToManyField(Role)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    groups = None
    user_permissions = None
    
    class Meta:
        db_table = "auth_user"
    
 
             
# class Role_User(models.Model):
#     # null=False? blank=True?
#     user = models.OneToOneField(User, on_delete=models.PROTECT)
#     role = models.OneToOneField(Role, on_delete=models.PROTECT)
    
#     class Meta:
#         db_table = "auth_user_role"
    



    