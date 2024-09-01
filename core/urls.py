from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.account.urls')),
    path('attendance/', include('apps.attendance.urls')),
    path('department/', include('apps.department.urls')),
    path('employees/', include('apps.employees.urls')),
    path('payroll/', include('apps.payroll.urls')),
    path('projects/', include('apps.projects.urls')),
    path('todo/', include('apps.todo.urls')),
    path('', include('apps.dashboard.urls')),
]
