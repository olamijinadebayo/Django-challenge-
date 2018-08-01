from django.db import models

# Create your models here.
class Person(models.Model):
    name= models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50,unique = True)
    timecreated = models.DateTimeField(auto_now=True)
