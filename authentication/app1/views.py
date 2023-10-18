from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')  
    else:
        form = CustomUserCreationForm()
    
    context = {  
        'form':form  
    }  
    return render(request, 'register.html', context) 
