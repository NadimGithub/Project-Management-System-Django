from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('<int:pk>/edit/', views.update_employee, name='update_employee'),
    path('<int:pk>/delete/', views.delete_employee, name='delete_employee'),
     path('<int:employee_id>/change_password/', views.change_password, name='change_password'),
]
