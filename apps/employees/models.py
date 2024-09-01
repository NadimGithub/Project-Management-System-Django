from django.db import models
from django.contrib.auth import get_user_model
from apps.department.models import Department

class Employee(models.Model):
    ROLE_CHOICES = [
        ('developer', 'Developer'),
        ('tester', 'Tester'),        
        ('hr', 'HR'),
        ('project_manager','Project Manager'),
        ('teamlead_dev', 'Team Lead (Dev)'),
        ('teamlead_qa', 'Team Lead (QA)'),
        ('ceo', 'CEO'),
        ('accountant', 'Accountant'),        
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    date_joined = models.DateField()
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='developer')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
