from django.urls import path
from . import views

urlpatterns = [
    path('',views.StoreView.as_view(),name='store'),
    path('productpage/<slug>',views.ItemDetailView.as_view(),name='productpage'),
    path('addtocart/<slug>',views.addtocart,name='addtocart'),
    # path('',views.store,name='store'),
    # path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
]
