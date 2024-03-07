from django.db import models

from django.contrib.auth.models import AbstractUser

class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    
    class Meta:
        db_table = "group"

class Account(AbstractUser):
    # roles = models.ManyToManyField(Role) # Убрать 0
    # orders = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    groups = None
    user_permissions = None
    
    class Meta:
        db_table = "auth_account"