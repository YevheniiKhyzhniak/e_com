from . import views
from django.urls import path, include
from products import views

urlpatterns = [
    # path("e_com_app/", views.e_com_app, name='e_com_app'),
    path("product/<product_id>", views.product, name='product'),
]
