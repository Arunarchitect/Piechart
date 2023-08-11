from django import forms
from .models import Costfinder

class CostfinderForm(forms.ModelForm):
    class Meta:
        model = Costfinder
        fields = [
            'area',
            'cost_choice',
        ]
        labels = {
            'area': 'Total Built-up Area (sq.ft)',  # Change 'Custom Area Label' to your desired label
            'cost_choice': 'Budgeting',  # Change 'Custom Cost Choice Label' to your desired label
        }
        widgets = {
            'cost_choice': forms.RadioSelect,  # Use the RadioSelect widget for cost_choice field
        }
    
