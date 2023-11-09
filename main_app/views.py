from django.shortcuts import render, redirect

from main_app.app_forms import EmployeeForm

from main_app.models import Employee

def home(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = EmployeeForm()
    return render(request, "employee.html", {"form": form})

def all_employees(request):
    employees = Employee.objects.all()
    return render(request, "all_employees.html", {'employees': employees})


def employee_details(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)
    return render(request, "employee_details.html", {'employee':employee})

