from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.
# class EmployeeCreate(CreateView):  
#     model = Employee  


class EmployeeCreate(ListView):
    model = Employee