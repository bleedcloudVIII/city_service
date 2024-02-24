from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Создаю свою модель вместо стандартной!!!!
class User(AbstractUser):
    role = models.CharField(max_length=128)
    
    
    groups = None
    user_permissions = None
    # username = None
    
    class Meta:
        db_table = "auth_user"
    
class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    
    class Meta:
        db_table = "auth_role"
        
class Role_User(models.Model):
    # null=False? blank=True?
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.OneToOneField(Role, on_delete=models.PROTECT)
    
    class Meta:
        db_table = "auth_user_role"
    



    