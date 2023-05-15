from django import forms
from .models import Qualification

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ['batch_number', 'location', 'date']