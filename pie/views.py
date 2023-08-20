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
            occupancy = cleaned_data['occupancy']

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
        occupancy = first_costfinder_entry.occupancy
        if occupancy == 'Residential':
            cost_factors = {
                'Ultra Low Cost': 1000,
                'Low Cost': 1500,
                'Medium': 2400,
                'Luxury': 2800,
                'Ultra Luxury': 3500,
            }
        elif occupancy == 'Commercial':
            cost_factors = {
                'Ultra Low Cost': 500,
                'Low Cost':1000,
                'Medium': 1500,
                'Luxury': 2000,
                'Ultra Luxury': 3000,
            }
        else:
            cost_factors = {
                'Ultra Low Cost': 1500,
                'Low Cost': 2000,
                'Medium': 2500,
                'Luxury': 3000,
                'Ultra Luxury': 3500,
            }

        cost = cost_factors[cost_choice] * area
        cost_split_label = ['Design and Approval', 'Footing and Foundation', 'Roof Slab', 'Flooring and Tiling', 'Water Supply and Plumbing', 'Excavation', 'RCC Work (Pillars, Columns, Slabs)', 'Brickwork and Plastering', 'Electric Wiring', 'Doors and Windows']
        cost_split = [
            0.025 * cost,  # Design and Approval
            0.125 * cost,  # Footing and Foundation
            0.125 * cost,  # Roof Slab
            0.1 * cost,    # Flooring and Tiling
            0.075 * cost,  # Water Supply and Plumbing
            0.075 * cost,  # Excavation
            0.175 * cost,  # RCC Work (Pillars, Columns, Slabs)
            0.125 * cost,  # Brickwork and Plastering
            0.075 * cost,  # Electric Wiring
            0.1 * cost     # Doors and Windows
            ]

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
        'cost_split' : cost_split,
        'cost_split_label' : cost_split_label,
        'occupancy' : occupancy,
    }

    return render(request, 'pie/result.html', context)


def about(request):
    return render(request,'pie/about.html')

def h(request):
    return render(request,'pie/home.html')


# excel_app/views.py

import xlwt
from django.http import HttpResponse
from .models import Costfinder  # Make sure to import your model here

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Costfinder Data')

    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Area in sq.ft', 'Budgeting', 'Building Type', 'Design and Approval', 'Footing and Foundation', 'Roof Slab', 'Flooring and Tiling', 'Water Supply and Plumbing', 'Excavation', 'RCC Work (Pillars, Columns, Slabs)', 'Brickwork and Plastering', 'Electric Wiring', 'Doors and Windows']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    costfinder_entries = Costfinder.objects.all()

    for entry in costfinder_entries:
        row_num += 1
        area = entry.area
        cost_choice = entry.cost_choice
        occupancy = entry.occupancy
        if occupancy == 'Residential':
            cost_factors = {
                'Ultra Low Cost': 1000,
                'Low Cost': 1500,
                'Medium': 2400,
                'Luxury': 2800,
                'Ultra Luxury': 3500,
            }
        elif occupancy == 'Commercial':
            cost_factors = {
                'Ultra Low Cost': 500,
                'Low Cost': 1000,
                'Medium': 1500,
                'Luxury': 2000,
                'Ultra Luxury': 3000,
            }
        else:
            cost_factors = {
                'Ultra Low Cost': 1500,
                'Low Cost': 2000,
                'Medium': 2500,
                'Luxury': 3000,
                'Ultra Luxury': 3500,
            }
        
        cost = cost_factors[cost_choice] * area
        cost_split_label = ['Design and Approval', 'Footing and Foundation', 'Roof Slab', 'Flooring and Tiling', 'Water Supply and Plumbing', 'Excavation', 'RCC Work (Pillars, Columns, Slabs)', 'Brickwork and Plastering', 'Electric Wiring', 'Doors and Windows']
        cost_split = [
            0.025 * cost,  # Design and Approval
            0.125 * cost,  # Footing and Foundation
            0.125 * cost,  # Roof Slab
            0.1 * cost,    # Flooring and Tiling
            0.075 * cost,  # Water Supply and Plumbing
            0.075 * cost,  # Excavation
            0.175 * cost,  # RCC Work (Pillars, Columns, Slabs)
            0.125 * cost,  # Brickwork and Plastering
            0.075 * cost,  # Electric Wiring
            0.1 * cost     # Doors and Windows
            ]
        cost_factor = cost_factors[cost_choice]

        data_row = [area, cost_choice, occupancy] + cost_split

        for col_num in range(len(data_row)):
            ws.write(row_num, col_num, data_row[col_num], font_style)

    wb.save(response)

    return response

