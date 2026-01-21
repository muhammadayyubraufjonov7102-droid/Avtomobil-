from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField 

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=True)

now = timezone.now()
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.DateField(default=now)
    mileage = models.PositiveIntegerField(default=0)
    engine_power = models.IntegerField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    
