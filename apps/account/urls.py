from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.role_based_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
