from django.http import HttpResponse
from django.urls import path, include
from . views import h, r, about, tools
urlpatterns = [
    path('',h , name= 'home'),
    path('result/',r, name='result' ),
    path('about/',about, name='about' ),
    path('tools/',tools, name='tools' ),
]