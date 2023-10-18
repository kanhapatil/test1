from django.shortcuts import render

# Home page view
def Home(request):
    return render(request, 'home.html')

# About page view
def About(request):
    return render(request, 'about.html')

# Menu page view (Admin db)
def Menu(request):
    return render(request, 'menu.html')

# Events page view
def Events(request):
    return render(request, 'events.html')

# Chefs page view (Admin db)
def Chefs(request): 
    return render(request, 'chefs.html')

# Gallery page view (Admin db)
def Gallery(request):
    return render(request, 'gallery.html')

# Contact page view
def Contact(request):
    return render(request, 'contact.html')

# Signup page view
def Signup(request):
    return render(request, 'signup.html')

# Login page view
def Login(request):
    return render(request, 'login.html')