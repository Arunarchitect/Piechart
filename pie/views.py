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

            real_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
            
            instance = form.save(commit=False)
            instance.ip_address = real_ip
            instance.save()
            return redirect('result')
    else:
        form = CostfinderForm()
    return render(request, "pie/tools.html", {'form': form})

def r(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip_address = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0]
    else:
        ip_address = request.META['REMOTE_ADDR']
    
    # Get the latest entry for the given IP address
    first_costfinder_entry = Costfinder.objects.filter(ip_address=ip_address).order_by('-timestamp').first()

    area = 0
    cost = 0
    cost_choice = ""
    occupancy = ""
    cost_factor = 0
    cost_split = []
    cost_split_label = []

    if first_costfinder_entry:
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

        cost_factor = cost_factors[cost_choice]
        cost = cost_factor * area

        # Construction Phase: Excavation
        cost_split_label = [
             'Design and Approval','Excavation & Site clearence', 'Footing and Foundation',
            'RCC Work (Pillars, Columns, Slabs)', 'Brickwork and Plastering',
            'Roof Slab', 'Flooring and Tiling', 'Water Supply and Plumbing',
            'Electric Wiring', 'Doors and Windows', 'Painting', 'Furnishing'
        ]

        cost_split = [
            0.025 * cost,   # Design and Approval 
            0.03 * cost,    # Excavation
            0.12 * cost,    # Footing and Foundation
            0.10 * cost,    # RCC Work (Pillars, Columns, Slabs)
            0.16 * cost,    # Brickwork and Plastering
            0.13 * cost,    # Roof Slab
            0.10 * cost,    # Flooring and Tiling
            0.05 * cost,    # Water Supply and Plumbing
            0.08 * cost,    # Electric Wiring
            0.08 * cost,    # Doors and Windows
            0.07 * cost,    # Painting
            0.055 * cost    # Furnishing
        ]

    context = {
        'area': area,
        'cost': cost,
        'cost_factor': cost_factor,
        'cost_choice': cost_choice,
        'cost_split': cost_split,
        'cost_split_label': cost_split_label,
        'occupancy': occupancy,
    }

    return render(request, 'pie/result.html', context)



def about(request):
    return render(request,'pie/about.html')

def h(request):
    return render(request,'pie/home.html')

def fun(request):
    return render(request,'pie/fun.html')

def realfun(request):
    return render(request,'pie/realfun.html')
# excel_app/views.py

import xlwt
from django.http import HttpResponse
from .models import Costfinder

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Costfinder Data')

    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
             'Built-up ARea (sq.ft)', 'Budgeting','Building Type','Design and Approval','Excavation & Site clearence', 'Footing and Foundation',
            'RCC Work (Pillars, Columns, Slabs)', 'Brickwork and Plastering',
            'Roof Slab', 'Flooring and Tiling', 'Water Supply and Plumbing',
            'Electric Wiring', 'Doors and Windows', 'Painting', 'Furnishing'
        ]


    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body
    font_style = xlwt.XFStyle()

    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip_address = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0]
    else:
        ip_address = request.META['REMOTE_ADDR']

    # Get the latest entry for the given IP address
    costfinder_entry = Costfinder.objects.filter(ip_address=ip_address).order_by('-timestamp').first()

    if costfinder_entry:
        area = costfinder_entry.area
        cost_choice = costfinder_entry.cost_choice
        occupancy = costfinder_entry.occupancy

        # Cost calculation based on occupancy and cost_choice
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

        cost_split = [
            0.025 * cost,   # Design and Approval 
            0.03 * cost,    # Excavation
            0.12 * cost,    # Footing and Foundation
            0.10 * cost,    # RCC Work (Pillars, Columns, Slabs)
            0.17 * cost,    # Brickwork and Plastering
            0.13 * cost,    # Roof Slab
            0.10 * cost,    # Flooring and Tiling
            0.05 * cost,    # Water Supply and Plumbing
            0.08 * cost,    # Electric Wiring
            0.08 * cost,    # Doors and Windows
            0.06 * cost,    # Painting
            0.055 * cost    # Furnishing
        ]



        data_row = [area, cost_choice, occupancy] + cost_split

        for col_num in range(len(data_row)):
            ws.write(row_num + 1, col_num, data_row[col_num], font_style)

    wb.save(response)

    return response
