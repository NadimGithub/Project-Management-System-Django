# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_list, name='attendance_list'),
    path('record/', views.record_attendance, name='record_attendance'),
    path('verify/<int:attendance_id>/', views.verify_attendance, name='verify_attendance'),
]
