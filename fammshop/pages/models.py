from django.db import models

from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    fullname=models.CharField(max_length=250,)
    email=models.EmailField(max_length=100)
    subject=models.TextField(blank=True,null=True)
    message=models.TextField(blank=True)

    def __str__(self):
        return self.email
