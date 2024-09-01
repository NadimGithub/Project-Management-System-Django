# views.py
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payroll
from .forms import PayrollForm
# from apps.employees.models import Employee

@login_required
def payroll_list(request):
    if request.user.is_superuser or request.user.groups.filter(name='Manager').exists():
        payrolls = Payroll.objects.all()
    else:
        payrolls = Payroll.objects.filter(employee__user=request.user)

    paginator = Paginator(payrolls, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'payroll/payroll_list.html', {'page_obj': page_obj})

@login_required
def create_payroll(request):
    if not (request.user.is_superuser or request.user.role == 'manager'):
        return redirect('payroll_list')

    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payroll_list')
    else:
        form = PayrollForm()

    return render(request, 'payroll/create_payroll.html', {'form': form})
