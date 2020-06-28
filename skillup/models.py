from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=65)


class Subject(models.Model):
    name = models.CharField(max_length=65)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Instructor(models.Model):
    fname = models.CharField(max_length=65)
    lname = models.CharField(max_length=65)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=255)
    designation = models.CharField(max_length=50)


class Course(models.Model):
    name = models.CharField(max_length=65)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    image_url = models.CharField(max_length=2083)
    preview_text = models.TextField(max_length=255, verbose_name='preview text')
    level = models.CharField(max_length=65)


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)


class MyEnrolledCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    course_name = models.CharField(max_length=65)
    level = models.CharField(max_length=65)


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=65)
    vid_url = models.CharField(max_length=2083)


class ContactMessage(models.Model):
    name = models.CharField(max_length=65)
    email = models.CharField(max_length=65)
    message = models.TextField()



