from django.db import models
from django.contrib.auth.models import AbstractUser
from companies.models import Order

class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    
    class Meta:
        db_table = "auth_role"  
        
class User(AbstractUser):
    roles = models.ManyToManyField(Role) # Убрать 0
    orders = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    
    groups = None
    user_permissions = None
    
    class Meta:
        db_table = "auth_user"
    