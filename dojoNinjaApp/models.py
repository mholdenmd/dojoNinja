# from os import name
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<Dojo object: {self.name} ({self.id})>"

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    fname= models.CharField(max_length=255)
    lname= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Ninja object: {self.fname} ({self.id})>"