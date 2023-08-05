from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CostfinderForm
# Create your views here.
    
def h(request):
    if request.method == 'POST':
        form = CostfinderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')  # Redirect to a success page after form submission
    else:
        form = CostfinderForm()  # Create an instance of the form for GET request
    return render(request, "pie/home.html", {'form': form})

def r(request):
    return render(request, "pie/result.html")