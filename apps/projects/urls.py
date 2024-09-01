from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('add/', views.add_project, name='add_project'),
    path('<int:project_id>/update/', views.update_project, name='update_project'),
    path('<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/<int:task_id>/update/', views.update_task, name='update_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]
