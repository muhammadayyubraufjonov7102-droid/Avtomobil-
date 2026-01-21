from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField 

class User(AbstractUser):
    phone_number = PhoneNumberField(unique=True)

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.PositiveIntegerField(default=0)
    engine_power = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    
