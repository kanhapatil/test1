from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=14)
    email = models.EmailField()
