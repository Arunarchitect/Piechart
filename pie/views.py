from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def h(request):
    return render(request, "pie/home.html")