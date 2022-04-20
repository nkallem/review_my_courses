from django import forms
from .models import Course, Review, School


class SchoolForm(forms.ModelForm):
    """Defines a form for School objects."""
    class Meta:
        model = School
        fields = ['name']
        labels = {'name': 'School name'}


class CourseForm(forms.ModelForm):
    """Defines a form for Course objects."""
    class Meta:
        model = Course
        fields = ['school', 'course_code', 'title']
        labels = {'title': 'Course title'}
        widgets = {'school': forms.HiddenInput()}
