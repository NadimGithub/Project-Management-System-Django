from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), 
                                                    ('manager', 'Manager'), 
                                                    ('employee', 'Employee')], default='employee')    
    groups = models.ManyToManyField(
        Group,
        related_name='account_user_set',  # Change related_name to avoid conflict
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='account_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='account_user_set',  # Change related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='account_user',
    )
