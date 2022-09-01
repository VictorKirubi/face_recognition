#Defines the URLs
#auto generated
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]