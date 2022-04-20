from django.db import models
from django.db.models import Avg
from django.core.exceptions import ValidationError
from datetime import date


# Validator function for the year
def validate_year(value):
    if 2000 <= value <= date.today().year:
        return value
    else:
        raise ValidationError("Year must be greater than or equal to 2000 and cannot exceed the current year.")


class School(models.Model):
    """The school that offers the course to be reviewed."""
    name = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the school."""
        return self.name

    @property
    def total_courses(self):
        """Return the count of courses for a school."""
        return self.course_set.count()

    @property
    def total_reviews(self):
        """Return the count of reviews for a school."""
        course_count = 0
        for course in self.course_set.all():
            course_count += course.total_reviews

        return course_count

    @property
    def average_workload(self):
        """Return the average workload for all reviews at the school."""
        workload_values = [review.workload for course in self.course_set.all() for review in course.review_set.all()]

        if len(workload_values) == 0:
            return None

        return round(sum(workload_values) / len(workload_values), 2)

    @property
    def average_difficulty(self):
        """Return the average difficulty for all courses at the school."""
        difficulty_values = [review.difficulty for course in self.course_set.all()
                             for review in course.review_set.all()]

        if len(difficulty_values) == 0:
            return None

        return round(sum(difficulty_values) / len(difficulty_values), 2)

    @property
    def average_rating(self):
        """Return the average rating for all courses at the school."""
        ratings = [review.rating for course in self.course_set.all() for review in course.review_set.all()]

        if len(ratings) == 0:
            return None

        return round(sum(ratings) / len(ratings), 2)


class Course(models.Model):
    """Represents a course that can be reviewed."""
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the course, including the course code and title."""
        return self.school.name + ": " + self.course_code + " - " + self.title

    def validate_unique(self, *args, **kwargs):
        super().validate_unique(*args, **kwargs)
        if self.__class__.objects.filter(school=self.school, course_code=self.course_code, title=self.title).exists():
            raise ValidationError(
                message='A course with this school, code, and title already exists.',
                code='Invalid Course',
            )

    @property
    def total_reviews(self):
        """Return the count of reviews for a course."""
        return self.review_set.count()

    @property
    def average_workload(self):
        """Return the average review rating of a course."""
        value = self.review_set.all().aggregate(Avg('workload'))['workload__avg']
        if value:
            value = round(value, 2)

        return value

    @property
    def average_difficulty(self):
        """Return the average review rating of a course."""
        value = self.review_set.all().aggregate(Avg('difficulty'))['difficulty__avg']
        if value:
            value = round(value, 2)

        return value

    @property
    def average_rating(self):
        """Return the average review rating of a course."""
        value = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
        if value:
            value = round(value, 2)

        return value


class Review(models.Model):
    """Represents a review of a course."""

    # Specify choices
    TERM_CHOICES = [
        ('FALL', 'Fall'),
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
    ]

    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    term = models.CharField(max_length=6, choices=TERM_CHOICES)
    year = models.PositiveIntegerField(validators=[validate_year], default=date.today().year)
    workload = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField(choices=RATING_CHOICES)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the course, including the course code and title."""
        return f"{self.course.school.name} ({self.course.course_code}): {self.text[:50]}..."

