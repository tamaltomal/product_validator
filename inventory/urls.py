from unicodedata import name
from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('item/<str:serial>', views.item, name='item'),
    ]