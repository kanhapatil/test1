from django.urls import path
from food import views

urlpatterns = [
    path("", views.Home, name='home'),
    path("about/", views.About, name='about'),
    path("menu/", views.Menu, name="menu"),
    path("events/", views.Events),
    path("chefs/", views.Chefs, name="chefs"),
    path("gallery/", views.Gallery, name="gallery"),
    path("contact/", views.Contact, name="contact"),
    path("signup/", views.Signup, name="signup"),
    path("login/", views.Login, name="login")
]