from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credits = models.PositiveIntegerField()

class Student(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in-progress', 'In Progress'),
    ]
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='in-progress')

    class Meta:
        unique_together = ['student', 'course']


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')