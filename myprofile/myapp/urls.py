from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('' ,views.index,name='home'),
    path('contact' , views.contact, name='contact')
]
