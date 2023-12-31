"""
URL configuration for main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_app import views
from django.conf.urls.static import static
from main_project import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name="home"),
    path('employees/', views.all_employees, name="employees"),
    path('search/', views.search_employees, name="search"),
    path('employees/<int:emp_id>', views.employee_details, name="details"),
    path('employees/delete/<int:emp_id>', views.employee_delete, name="delete"),
    path('employees/update/<int:emp_id>', views.employee_update, name="update"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# tables
# kavete kavete@gmail.com 54321