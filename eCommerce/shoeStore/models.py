from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Shoe(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    image=models.ImageField(upload_to="shoe_images")
    description=models.CharField(max_length=1000,default="True")

    def __str__(self) -> str:
        return f"{self.name} {self.price}"
class PaymentInfo(models.Model):
    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address=models.CharField(max_length=200)
    card_number=models.CharField(max_length=400)
    month=models.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(1)])
    date=models.CharField(max_length=100,null=True)
class NewsLetter(models.Model):
    email=models.EmailField(max_length=200)