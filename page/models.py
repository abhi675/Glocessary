from django.db import models
from django.db.models.fields import IntegerField


class Shop(models.Model):
    price=models.IntegerField(default=0)
    productname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='items')

    def __str__(self):
        return self.productname



class Details(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return "{} - {}".format(self.name,self.email)


class Payment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.TextField()
    nameoncard=models.CharField(max_length=50)
    creditcardnumber=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    cvv=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    productname=models.CharField(max_length=50)

    def __str__(self):
        return "{}  {}".format(self.name,self.email)