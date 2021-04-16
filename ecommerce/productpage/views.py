from django.shortcuts import render
from store.models import FoodItems
from store import views
# Create your views here.

def muruku(request):
    item = FoodItems.objects.get(name='muruku')
    return render(request,'productpage/productpage.html', {'item' : item})

def BesanLadoo(request):
    item = FoodItems.objects.get(name='BesanLadoo')
    return render(request,'productpage/productpage.html', {'item' : item})

def PeanutChikki(request):
    item = FoodItems.objects.get(name='PeanutChikki')
    return render(request,'productpage/productpage.html', {'item' : item})
