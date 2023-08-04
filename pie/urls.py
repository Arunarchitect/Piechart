from django.http import HttpResponse
from django.urls import path, include
from . views import h
urlpatterns = [
    path('',h ),
]