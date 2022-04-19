from django.shortcuts import render
from .models import Course, School, Review


def index(request):
    """The home page for Review My Courses."""
    return render(request, 'review_my_courses/index.html')


def schools(request):
    """Show all schools."""
    schools = School.objects.order_by('name')
    context = {'schools': schools}
    return render(request, 'review_my_courses/schools.html', context)

def school(request, school_id):
    """Show a school and all its associated courses."""
    school = School.objects.get(id=school_id)
    courses = school.course_set.order_by('course_code')
    context = {'school': school, 'courses': courses}
    return render(request, 'review_my_courses/school.html', context)

def course(request, course_id):
    """Show all reviews for a single course."""
    course = Course.objects.get(id=course_id)
    school = course.school
    reviews = course.review_set.order_by('-review_date')
    context = {'school': school, 'course': course, 'reviews': reviews}
    return render(request, 'review_my_courses/course.html', context)