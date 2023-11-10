# Generated by Django 4.2.7 on 2028-01-01 05:24

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0002_employee_created_at_employee_profile_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="profile",
            field=models.ImageField(
                default="employees/default.jpg",
                null=True,
                upload_to=main_app.models.unique_img_name,
            ),
        ),
    ]
