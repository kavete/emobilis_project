from django.core.management import BaseCommand
import os
from main_project import settings
from main_app.models import Employee
import json

class Command(BaseCommand):
    help = "Populate the employee table with 1000 records"
    
    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'employees.json')
        self.stdout.write(
            self.style.SUCCESS("Started to import data")
        )
        with open(path) as file: # file = open(path)
            employees = json.load(file)
            for employee in employees:
                Employee.objects.create(
                    name=employee['name'],
                    email=employee['email'],
                    dob=employee['dob'],
                    salary=employee['salary'],
                    disabled=employee['disbled'],
                )
        self.stdout.write(
            self.style.SUCCESS("Data populated successfuly")
        )
                