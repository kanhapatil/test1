from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Colors(BaseModel):
    color_code = models.CharField(max_length=100) 

class People(BaseModel):
    name = models.CharField(max_length=100)
    about = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    colors = models.ManyToManyField(Colors)

class PeopleAddress(BaseModel):
    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="address")
    address = models.TextField() 