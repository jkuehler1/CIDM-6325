from django.shortcuts import render
from .models import Course, Student, Enrollment


def list_courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'degree_checklist/courses_list.html', context)


def list_students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'degree_checklist/students_list.html', context)


def list_enrollments(request):
    enrollments = Enrollment.objects.all().select_related('student', 'course')
    context = {'enrollments': enrollments}
    return render(request, 'degree_checklist/enrollments_list.html', context)

def all_records(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    enrollments = Enrollment.objects.all().select_related('student', 'course')
    context = {
        'courses': courses,
        'students': students,
        'enrollments': enrollments
    }
    return render(request, 'degree_checklist/all_records.html', context)

