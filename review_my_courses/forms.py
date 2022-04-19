from django import forms
from .models import Course, Review, School


class SchoolForm(forms.ModelForm):
    """Defines a form for School objects."""
    class Meta:
        model = School
        fields = ['name']
        labels = {'name' : 'School name'}