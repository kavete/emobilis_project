from django import forms
from main_app.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "dob" : forms.DateInput(attrs={"type": "date", "min": "1960-12-31", "max":"2005-12-31"}),
            "salary": forms.NumberInput(attrs={"max": 100000, "min": 20000}),
        }
        labels = {
            "dob": "Date of Birth",
            "email": "Email Address",
        }
