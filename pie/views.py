import os
import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from .forms import CostfinderForm
from .models import Costfinder
from django.conf import settings

def h(request):
    if request.method == 'POST':
        form = CostfinderForm(request.POST)
        if form.is_valid():
            # Delete previous data entry
            Costfinder.objects.all().delete()

            # Delete previous image if it exists
            previous_image_path = 'pie/static/pie/image.png'  # Replace with the actual path used before
            if os.path.exists(previous_image_path):
                os.remove(previous_image_path)

            # Create and save the new pie chart image
            
            # Combine the prefixes with the values and format them to 2 decimal places
            

            cleaned_data = form.cleaned_data
            d = cleaned_data['area']
            c= d*3000
            x = [0.10 * c, 0.10 * c, 0.10 * c, 0.25 * c, 0.25 * c, 0.20 * c]
            prefixes = ['electrical_cost:', 'plumbing_cost:', 'Furnishing_cost:', 'structural_cost:', 'finishes_cost:', 'other_costs:']
            x_ = [int(val) for val in x]

            labels = [f'{prefix}{val}' for prefix, val in zip(prefixes, x_)]
            plt.pie(x, labels=labels)
            plt.savefig( 'pie/static/pie/image.png')  # Save the new plot as an image
            plt.close()  # Close the plot to release resources

            form.save()
            return redirect('result')  # Redirect to a success page after form submission
    else:
        form = CostfinderForm()  # Create an instance of the form for GET request
    return render(request, "pie/home.html", {'form': form})


def r(request):
    first_costfinder_entry = Costfinder.objects.first()
    area = first_costfinder_entry.area
    c = area*3000
    return render(request, 'pie/result.html', {'area': area,'cost':c})

