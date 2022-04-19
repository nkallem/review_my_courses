"""Defines URL patterns for review_my_courses."""

from django.urls import path

from . import views

app_name = 'review_my_courses'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all schools.
    path('schools/', views.schools, name='schools'),
    # Detail page for a single school.
    path('schools/<int:school_id>/', views.school, name='school'),
    # Detail page for a single course.
    path('courses/<int:course_id>/', views.course, name='course'),
    # Page for adding a new school.
    path('new_school/', views.new_school, name='new_school'),
]