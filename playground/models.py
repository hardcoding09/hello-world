from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)