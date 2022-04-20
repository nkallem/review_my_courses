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
    # Page for adding a new course.
    path('new_course/<int:school_id>/', views.new_course, name='new_course'),
    # Page for adding a new review.
    path('new_review/<int:course_id>/', views.new_review, name='new_review'),
    # Page for editing a school.
    path('edit_school/<int:school_id>/', views.edit_school, name='edit_school'),
    # Page for editing a course.
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
]
