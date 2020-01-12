from django import forms
from .models import Report


class ReportCreationForm(forms.ModelForm):
    
    class Meta:
        model = Report
        fields = [
            
            'sector',
            'kpi',
            
            'from_to_date',
            'up_to_date',
            'notes',
            
        ]

