from django import forms 
from . import models
class Category(forms.ModelForm):
    class Meta:
        model=models.TaskCategory
        fields='__all__'
