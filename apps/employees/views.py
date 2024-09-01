from django.shortcuts import render, redirect, get_object_or_404
from django.core.cache import cache
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully.")
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully.")
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, "Employee deleted successfully.")
        return redirect('employee_list')
    return render(request, 'employees/delete_employee.html', {'employee': employee})

@login_required
def employee_list(request):
    employees = Employee.objects.all()

    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    employee_data = []

    for employee in page_obj:
        password = cache.get(f'user_password_{employee.pk}')
        print(password)
        employee_data.append({
            'employee': employee,
            'password': password
        })

    return render(request, 'employees/employee_list.html', {
        'employee_data': employee_data,
        'page_obj': page_obj,
    })

def superadmin_check(user):
    return user.is_superuser

@user_passes_test(superadmin_check)
def change_password(request, employee_id):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        if new_password:
            employee = get_object_or_404(Employee, pk=employee_id)
            user = employee.user
            user.set_password(new_password)
            user.save()
            messages.success(request, f"Password for {employee.first_name} {employee.last_name} has been changed.")
        else:
            messages.error(request, "Password cannot be empty.")
    return redirect('employee_list')
