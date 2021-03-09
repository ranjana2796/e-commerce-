from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=50)
    original_price=models.IntegerField()
    discounted_price=models.IntegerField()
    category=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    image=models.CharField(max_length=200)
