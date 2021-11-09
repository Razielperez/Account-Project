from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length = 60)
    lastName = models.CharField(max_length=60)
    userName= models.CharField(max_length = 60,primary_key=True)
    password= models.CharField(max_length = 60)
    email= models.CharField(max_length=60)
    phoneNumber= models.CharField(max_length = 60)
    def __str__(self):
        return f'User name:{self.firstName}'

# Create your models here.

