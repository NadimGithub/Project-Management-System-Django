from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Employee
from .forms import EmployeeForm
from django.core.cache import cache

User = get_user_model()

class EmployeeTests(TestCase):
    
    def setUp(self):
        # Create a superuser for testing
        self.superuser = User.objects.create_superuser(
            username='admin',
            password='adminpass',
            email='admin@example.com'
        )
        
        # Create a normal user
        self.user = User.objects.create_user(
            username='user',
            password='userpass',
            email='user@example.com'
        )
        
        # Create an employee associated with the superuser
        self.employee = Employee.objects.create(
            user=self.superuser,
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone='1234567890',
            address='123 Main St',
            department=None,  # Assuming you have a Department model
            position='Developer',
            date_joined='2024-01-01',
            is_active=True
        )
        
        self.client = Client()
    
    def test_add_employee(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('add_employee'), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com',
            'phone': '0987654321',
            'address': '456 Elm St',
            'department': '',  # Assuming the department is optional
            'position': 'Designer',
            'date_joined': '2024-02-01',
            'is_active': True,
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.assertTrue(Employee.objects.filter(email='jane.doe@example.com').exists())
    
    def test_update_employee(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('update_employee', args=[self.employee.pk]), {
            'first_name': 'Johnathan',
            'last_name': 'Doe',
            'email': 'johnathan.doe@example.com',
            'phone': '1234567890',
            'address': '123 Main St',
            'department': '',  # Assuming the department is optional
            'position': 'Senior Developer',
            'date_joined': '2024-01-01',
            'is_active': True,
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.first_name, 'Johnathan')
        self.assertEqual(self.employee.email, 'johnathan.doe@example.com')
    
    def test_delete_employee(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('delete_employee', args=[self.employee.pk]))
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.assertFalse(Employee.objects.filter(pk=self.employee.pk).exists())
    
    def test_employee_list(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.employee.first_name)
        self.assertContains(response, self.employee.email)
    
    def test_change_password(self):
        self.client.login(username='admin', password='adminpass')
        new_password = 'newpassword123'
        response = self.client.post(reverse('change_password', args=[self.employee.pk]), {
            'new_password': new_password
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful POST
        self.employee.user.refresh_from_db()
        self.assertTrue(self.employee.user.check_password(new_password))
    
    def test_user_cannot_access_admin_views(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 403)  # Forbidden, since the user is not a superuser

    def test_cache_password(self):
        # Set a password in the cache
        cache.set(f'user_password_{self.employee.pk}', 'testpassword', timeout=60)
        self.assertEqual(cache.get(f'user_password_{self.employee.pk}'), 'testpassword')

    def test_login_required(self):
        response = self.client.get(reverse('employee_list'))
        self.assertRedirects(response, '/accounts/login/?next=/employees/')  # Check for redirection to login
