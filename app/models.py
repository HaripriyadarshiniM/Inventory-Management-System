from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Supplier(models.Model):
    name=models.CharField(max_length=100)
    contact_email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)

    sku = models.CharField(max_length=30, unique=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    quantity_in_stock = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name


