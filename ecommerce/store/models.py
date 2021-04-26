from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class FoodItems(models.Model):
    name  = models.CharField(max_length=100)
    img   = models.ImageField(upload_to='images')
    desc  = models.TextField()
    price = models.IntegerField()
    piece = models.IntegerField()
    offer = models.BooleanField(default=False)
    discountprice = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:productpage",kwargs={
        'slug': self.slug
        })

class OrderItem(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default = False)
    item = models.ForeignKey(FoodItems, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return 'f"{self.quantity} of {self.item.name}"'

class Order(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add = True )
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default = False)

    def __str__():
        return self.user.username
