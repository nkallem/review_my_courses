from django.shortcuts import render, redirect
from .models import Course, School, Review
from .forms import CourseForm, SchoolForm


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


def new_school(request):
    """Add a new school"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = SchoolForm()
    else:
        # POST data submitted; process data.
        form = SchoolForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_my_courses:schools')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'review_my_courses/new_school.html', context)


def new_course(request, school_id):
    """Add a new course"""
    school = School.objects.get(id=school_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CourseForm(initial={'school': school})
    else:
        # POST data submitted; process data.
        form = CourseForm(data=request.POST, initial={'school': school})
        if form.is_valid():
            form.save()
            return redirect('review_my_courses:school', school_id=school_id)

    # Display a blank or invalid form
    context = {'school': school, 'form': form}
    return render(request, 'review_my_courses/new_course.html', context)
