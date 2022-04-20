# Generated by Django 4.0.4 on 2022-04-20 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_my_courses', '0004_course_unique_course'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='course',
            name='unique_course',
        ),
        migrations.AddConstraint(
            model_name='course',
            constraint=models.UniqueConstraint(fields=('school', 'title', 'course_code'), name='unique_course'),
        ),
    ]
