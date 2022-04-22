# Review My Courses

## Author

This project was developed by Nicholas Kallem (nwk0006@auburn.edu).

## Introduction

This is a school course review and rating website developed for a final project
in CPSC 4970: Python at Auburn University. The website was created using Python
and the Django framework, and it was styled using Bootstrap 5.

The website can be viewed here:

[Review My Courses](https://review-my-courses.herokuapp.com/)

## Project Specifications

The Django option for the final project required the development of an 
application that edits a three-level model. For this website, the model allows
the editing of the following levels:

* School
* Course
* Review

You can create, edit, and delete objects at each level of the model.

---

## Managing and Viewing Schools
### Viewing All Schools
After navigating to the [main website](https://review-my-courses.herokuapp.com/),
click on **View Schools** to view the list of all schools in the database.

Along with each school's name, the table will list the following information:
* Total number of courses for the school
* Total number of review for the school
* Average difficulty of the courses
* Average workload of the courses
* Average course rating

The [schools page](https://review-my-courses.herokuapp.com/schools/) also
provides the following links:
1. Add New School
2. View the School (displays the courses page for that school)
3. Edit the School
4. Delete the School

### Adding a New School

Click on the **Add New School** button to a add a school to the list. You must
fill out the school name, and the name cannot match an existing school.

### View a School

To view the course list for a specific school, click the **View** button for the
school.

### Edit a School

To edit the name of a school, click the **Edit** button. The new name cannot
match an existing school in the database.

### Delete a School

To delete a school, click the **Delete** button.

---

## Managing and Viewing Courses

### Viewing Courses for a School

To view the courses for a given school, click on the **View** button from the 
Schools page. The courses for the selected school will be displayed in a table,
along with:
* Total number of reviews for the course
* Average difficulty of the course
* Average workload of the course
* Average course rating

The school's courses page also provides the following links:
1. Add New Course
2. View the Course (displays the reviews page for that course)
3. Edit the Course
4. Delete the Course

### Adding a New Course

Click on the **Add New Course** button to a add a course to the list. You must
fill out the course code (for example, CPSC 4970) and the course title. 
For each course, the combination of school, course title, and course code must
be unique.

### View a Course

To view the review list for a specific course, click the **View** button for the
course.

### Edit a Course

To edit the course code and title on an existing course, click the **Edit** 
button. A school cannot have duplicate courses with the same course code and
title.

### Delete a Course

To delete a course, click the **Delete** button.

---

## Managing and Viewing Reviews

### Viewing Reviews for a Course

To view the reviews for a given course, click on the **View** button from the 
Courses page. The reviews for the selected course will be displayed. Each review
includes:
* School Name
* Course Code and Title
* Term and Year
* Review Date
* Average weekly workload (in hours/week)
* Difficulty rating (1-5)
* Overall rating (1-5)
* Text review

The Reviews page also provides the following links:
1. Add New Review
2. Edit the Review
3. Delete the Review

### Adding a New Review

Click on the **Add New Review** button to add a review to the course. Fill out
each of the required fields and click **Submit review** to add the review.

### Edit a Review

To edit a review, click the **Edit** button. 

### Delete a Review

To delete a review, click the **Delete** button.