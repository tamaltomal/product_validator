from unicodedata import name
from django.urls import path

from . import views

app_name = 'validate'
urlpatterns = [
    path('<str:code>/', views.validate, name='validate'),
    ]