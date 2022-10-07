from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)


class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
