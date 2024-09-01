from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Employee
import random
import string
from django.contrib.auth import get_user_model

def generate_random_password(length=8):
    """Generate a random password."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@receiver(post_save, sender=Employee)
def create_user_for_employee(sender, instance, created, **kwargs):
    if created:
        User = get_user_model()

        username = f"{instance.first_name.lower()}.{instance.last_name.lower()}"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        print('password from signal: ',password)

        user = User.objects.create_user(username=username, password=password, email=instance.email)
        
        instance.user = user
        instance.save()
        
        cache.set(f'user_password_{instance.pk}', password, timeout=3600)
        

