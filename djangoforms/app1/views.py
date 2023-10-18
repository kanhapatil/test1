from django.shortcuts import render
from .form import EmployeeForm

# Create your views here.
def Index(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    return render(request, 'home.html', {'form':form})