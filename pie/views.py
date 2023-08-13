# import os
# import matplotlib.pyplot as plt
# from django.shortcuts import render, redirect
# from .forms import CostfinderForm
# from .models import Costfinder
# from django.conf import settings

# #PIECHART CODE
# def h(request):
#     if request.method == 'POST':
#         form = CostfinderForm(request.POST)
       
#         if form.is_valid():
#             # Delete previous data entry
#             Costfinder.objects.all().delete()

#             # Delete previous image if it exists
#             # previous_costfinder = Costfinder.objects.first()
#             # if previous_costfinder and previous_costfinder.image:
#             #     previous_costfinder.image.delete()  # Delete the associated image file
#             #     previous_costfinder.delete()  # Delete the database entry

#             # Create and save the new pie chart image
#             cleaned_data = form.cleaned_data
#             cost_choice = cleaned_data['cost_choice']
#             area = cleaned_data['area']

#             cost_factors = {
#                 'Ultra Low Cost': 2000,
#                 'Low Cost': 2500,
#                 'Medium': 3000,
#                 'Luxury': 3500,
#                 'Ultra Luxury': 4000,
#                 }
#             cost = cost_factors[cost_choice] * area
            
#             x = [0.10 * cost, 0.10 * cost, 0.10 * cost, 0.25 * cost, 0.25 * cost, 0.20 * cost]
#             prefixes = ['Electrical Cost: ', 'Plumbing Cost: ', 'Furnishing Cost: ', 'Structural Cost: ', 'Finishes Cost: ', 'Other Costs: ']
#             x_ = [int(val) for val in x]

#             labels = [f'{prefix}{val}' for prefix, val in zip(prefixes, x_)]
#             plt.pie(x, labels=labels)

#             # Save the new plot as an image in the media directory
#             image_path = os.path.join(settings.MEDIA_ROOT, 'image.png')
#             plt.savefig(image_path)
#             plt.close()  # Close the plot to release resources

#             # Save the image path to the 'image' field of the Costfinder model
#             # new_costfinder = Costfinder.objects.create(area=area)
#             # new_costfinder.image = 'image.png'
#             # new_costfinder.save()

#             form.save()
#             return redirect('result')  # Redirect to a success page after form submission
#     else:
#         form = CostfinderForm()  # Create an instance of the form for GET request
#     return render(request, "pie/home.html", {'form': form})

#BAR CHART CODE
import os
import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render, redirect
from .forms import CostfinderForm
from .models import Costfinder
from django.conf import settings

def tools(request):
    if request.method == 'POST':
        form = CostfinderForm(request.POST)
       
        if form.is_valid():
            Costfinder.objects.all().delete()

            cleaned_data = form.cleaned_data
            cost_choice = cleaned_data['cost_choice']
            area = cleaned_data['area']

            cost_factors = {
                'Ultra Low Cost': 2000,
                'Low Cost': 2500,
                'Medium': 3000,
                'Luxury': 3500,
                'Ultra Luxury': 4000,
            }
            cost = cost_factors[cost_choice] * area

            factors = ['Electrical Cost', 'Plumbing Cost', 'Furnishing Cost', 'Structural Cost', 'Finishes Cost', 'Other Costs']
            x = [0.10 * cost, 0.10 * cost, 0.10 * cost, 0.25 * cost, 0.25 * cost, 0.20 * cost]

            colors = ['blue', 'green', 'purple', 'orange', 'red', 'cyan']

            plt.barh(factors, x, color=colors)
            plt.xlabel('Cost (₹)')
            plt.ylabel('Cost Factors')
            plt.title('Cost Breakdown')

            plt.gca().invert_yaxis()
            plt.tight_layout()

            for index, value in enumerate(x):
                value_str = f"  ₹ {value:.2f}"
                bar_width = 20  # Adjust width for text fitting
                plt.text(bar_width, index, value_str, color='black', fontsize=10, va='center')

            image_path = os.path.join(settings.MEDIA_ROOT, 'image.png')
            plt.savefig(image_path)
            plt.close()

            form.save()
            return redirect('result')
    else:
        form = CostfinderForm()
    return render(request, "pie/tools.html", {'form': form})

def r(request):
    first_costfinder_entry = Costfinder.objects.first()

    if first_costfinder_entry and first_costfinder_entry.image:
        area = first_costfinder_entry.area
        cost_choice = first_costfinder_entry.cost_choice
        cost_factors = {
                'Ultra Low Cost': 2000,
                'Low Cost': 2500,
                'Medium': 3000,
                'Luxury': 3500,
                'Ultra Luxury': 4000,
                }
        cost = cost_factors[cost_choice] * area
        cost_factor = cost_factors[cost_choice]
        image_url = "/media/image.png"
    else:
        area = 0
        cost = 0
        image_url = None

    context = {
        'area': area,
        'cost': cost,
        'cost_factor': cost_factor,
        'cost_choice': cost_choice,
        'image_url': image_url,
    }

    return render(request, 'pie/result.html', context)


def about(request):
    return render(request,'pie/about.html')

def h(request):
    return render(request,'pie/home.html')