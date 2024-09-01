# urls.py in the todo app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('<int:todo_id>/update/', views.update_todo, name='update_todo'),
    path('<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
]
