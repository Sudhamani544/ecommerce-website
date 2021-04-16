from django.shortcuts import render
from .models import FoodItems
# Create your views here.

def store(request):
    items = FoodItems.objects.all()
    return render(request,'store/store.html', {'items' : items})

def cart(request):
    context = {}
    return render(request,'store/cart.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
