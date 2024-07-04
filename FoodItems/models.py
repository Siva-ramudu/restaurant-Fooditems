from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fooditems(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    foodtype=models.CharField(max_length=10)
    image = models.ImageField( upload_to = "fooditems")
    Recipe = models.FileField( upload_to = "fooditems")


    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=30)
    dob = models.DateField()
    uid = models.OneToOneField(User, on_delete=models.CASCADE)
