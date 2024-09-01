# models.py
from django.db import models
from apps.employees.models import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_attendance')

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.date}"
