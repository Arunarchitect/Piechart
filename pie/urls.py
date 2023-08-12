from django.http import HttpResponse
from django.urls import path, include
from . views import h, r, about
urlpatterns = [
    path('',h , name= 'home'),
    path('result/',r, name='result' ),
    path('about/',about, name='about' ),
]