from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
       
    def __str__(self):
        return self.username