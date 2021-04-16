from django.urls import path
from . import views

urlpatterns = [
    path('muruku/',views.muruku,name="muruku"),
    path('BesanLadoo/',views.BesanLadoo,name="BesanLadoo"),
    path('PeanutChikki/',views.PeanutChikki,name="PeanutChikki"),
]
