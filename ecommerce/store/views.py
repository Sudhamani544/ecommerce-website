from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import FoodItems, OrderItem, Order
from django.utils import timezone
# Create your views here.

class StoreView(ListView):
    model = FoodItems
    template_name = "store/store.html"

# def store(request):
#     items = FoodItems.objects.all()
#     return render(request,'store/store.html', {'items' : items})

class ItemDetailView(DetailView):
    model = FoodItems
    template_name = 'store/productpage.html'

# def muruku(request):
#     item = FoodItems.objects.get(name='muruku')
#     return render(request,'productpage/productpage.html', {'item' : item})

def addtocart(request, slug):
    item = get_object_or_404(FoodItems,slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user,ordered = False)
    if order_qs.exists():
        order=order_qs[0]
        #check if the order item in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order_date = timezone.now()
        order= Order.objects.create(user=request.user)
        order.items.add(order_item)
    return redirect("store:productpage",slug = slug)

def cart(request, slug):
    items = FoodItems.Objects.all(slug=slug)
    return render(request,'store/cart.html',{'items':items})

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
