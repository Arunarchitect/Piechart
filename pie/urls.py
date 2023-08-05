from django.http import HttpResponse
from django.urls import path, include
from . views import h, r
urlpatterns = [
    path('',h ),
    path('result/',r, name='result' ),
]