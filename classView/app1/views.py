from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import ContactForm

# Function based view
def myview(request):
    return HttpResponse("<h1>Function based view</h1>")

# Class based view
class MyView(View):
    def get(self, request):
        return HttpResponse("<h1>Class based view - GET</h1>")
    

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class AboutClassView(View):
    def get(self, request):
        context = {
            'msg' : 'Welcome kanha patil'
        }
        return render(request, 'home.html', context)
    

class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'home.html', {'form':form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("<h2>Thank you for submitted</h2>")

# Template view used to render static page, which is not connect with database
from django.views.generic.base import TemplateView
class AboutView(TemplateView):
    template_name = "about.html"