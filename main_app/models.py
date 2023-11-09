from django.db import models
import os, uuid
# Create your models here.

def unique_img_name(instance, filename):
    name = uuid.uuid4()
    print(name)
    ext = filename.split(".")[-1]
    full_name = f"{name}.{ext}"
    return os.path.join('employees', full_name)
    
class Employee(models.Model):
    # name, email, dob, salary, disabled
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    disabled = models.BooleanField(default=False)
    profile = models.ImageField(upload_to=unique_img_name, null=True, default="employees/default.jpg")
    created_at = models.DateTimeField(auto_now_add=True, null=True) # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True) # Everytime an update happens


    def __str__(self):
        return self.name