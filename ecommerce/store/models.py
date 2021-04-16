from django.db import models

# Create your models here.
class FoodItems(models.Model):
    name  = models.CharField(max_length=100)
    img   = models.ImageField(upload_to='images')
    desc  = models.TextField()
    price = models.IntegerField()
    piece = models.IntegerField()
    offer = models.BooleanField(default=False)
