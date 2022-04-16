from django.shortcuts import render


def index(request):
    """The home page for Review My Courses."""
    return render(request, 'review_my_courses/index.html')
