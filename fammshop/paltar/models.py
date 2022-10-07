from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=100,null=True)
    slug=models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.slug


class Description(models.Model):
    product_features=models.TextField(blank=True,null=True)
    product_detail=models.TextField(blank=True,null=True)
    about_brend=models.TextField(blank=True,null=True)
    editor_note=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.product_detail[:30]




class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=1000)
    client=models.ManyToManyField(User, related_name="product_client" ,blank=True)
    description=models.ForeignKey(Description,on_delete=models.DO_NOTHING,null=True)
    category=models.ManyToManyField(Category)
    image=models.ImageField()
    model=models.CharField(max_length=200,null=True)
    size=models.CharField(max_length=20)
    avaliable=models.BooleanField(default=True)
    add_date=models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return self.name
