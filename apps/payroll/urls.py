# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_list, name='payroll_list'),
    path('create/', views.create_payroll, name='create_payroll'),
]
