from django import forms
from .models import Employee
from apps.department.models import Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 
                  'phone', 'address', 'department', 'position', 
                  'date_joined', 'is_active', 'role']

        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'date_joined': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # To populate department choices in the form
        self.fields['department'].queryset = Department.objects.all()
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        
