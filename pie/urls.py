from django.http import HttpResponse
from django.urls import path, include
from . views import h, r, about, tools, export_users_xls, realfun, fun
urlpatterns = [
    path('',h , name= 'home'),
    path('result/',r, name='result' ),
    path('about/',about, name='about' ),
    path('tools/',tools, name='tools' ),
    path('export/excel', export_users_xls, name='export_excel'),
    path('fun/',fun, name='fun' ),
    path('plan/',realfun, name='plan' ),
]