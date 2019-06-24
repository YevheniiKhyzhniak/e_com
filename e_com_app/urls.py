from . import views
from django.urls import path, include

urlpatterns = [
    path('e_com_app/', views.e_com_app, name='e_com_app'),
]
