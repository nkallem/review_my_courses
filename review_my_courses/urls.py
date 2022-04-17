"""Defines URL patterns for review_my_courses."""

from django.urls import path

from . import views

app_name = 'review_my_courses'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all schools.
    path('schools/', views.schools, name='schools'),
]