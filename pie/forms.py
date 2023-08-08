from django import forms
from .models import Costfinder

class CostfinderForm(forms.ModelForm):
    class Meta:
        model = Costfinder
        fields = [
            'area',
        ]
    
