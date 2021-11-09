from django.db import models


class File (models.Model):
   user = models.CharField(max_length=100)
   name = models.CharField(max_length=100)
   file = models.FileField(upload_to='media/')
   date = models.DateField(auto_now_add=True)
   

