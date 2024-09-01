# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Attendance
from apps.employees.models import Employee
from .forms import AttendanceForm

@login_required
def attendance_list(request):
    try:
        employee = request.user.employee
    except Employee.DoesNotExist:
        return render(request, 'attendance/attendance_list.html', {'attendances': []})

    if employee.role in ['project_manager', 'teamlead_dev', 'teamlead_qa', 'ceo','hr']:
        attendances = Attendance.objects.all()
    else:
        attendances = Attendance.objects.filter(employee=employee)
    
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})

@login_required
def record_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.employee = request.user.employee
            attendance.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/record_attendance.html', {'form': form})

@login_required
def verify_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    role = request.user.employee.role
    allowed_role = ['hr','project_manager','ceo']
    if role in allowed_role :
        attendance.is_verified = True
        attendance.verified_by = request.user.employee
        attendance.save()
        return redirect('attendance_list')
    else:
        return redirect('attendance_list')
