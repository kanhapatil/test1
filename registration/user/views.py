from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, 'user/index.html', {'title':'index'})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

    return render(request, 'user/register.html', {'title':'register here'})