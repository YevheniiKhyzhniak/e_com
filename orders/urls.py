from . import views
from django.urls import path, include

urlpatterns = [
    path("cart_adding/", views.cart_adding, name='cart_adding'),
    path("checkout/", views.checkout, name='checkout'),
]
