from django.db import models

# Create your models here.

class Product(models.Model):
    # id: int
    title= models.TextField()
    price= models.PositiveIntegerField()
    img = models.ImageField(upload_to = 'pictures')
    offer= models.BooleanField(default = False)
    