from django.shortcuts import render, redirect
from .models import Course, Student, Enrollment
from .forms import CourseForm, StudentForm, EnrollmentForm


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm()
    return render(request, 'degree_checklist/add_course.html', {'form': form})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'degree_checklist/add_student.html', {'form': form})


def add_enrollment(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_enrollments')
    else:
        form = EnrollmentForm()
    return render(request, 'degree_checklist/add_enrollment.html', {'form': form})


def list_courses(request):
    sort = request.GET.get('sort', 'name')
    courses = Course.objects.all().order_by(sort)
    context = {'courses': courses}
    return render(request, 'degree_checklist/courses_list.html', context)


def list_students(request):
    order_by = request.GET.get('order_by', 'last_name')
    students = Student.objects.all().order_by(order_by)
    context = {'students': students}
    return render(request, 'degree_checklist/students_list.html', context)


def list_enrollments(request):
    sort = request.GET.get('sort', 'date_enrolled')
    enrollments = Enrollment.objects.all().select_related(
        'student', 'course').order_by(sort)
    context = {'enrollments': enrollments}
    return render(request, 'degree_checklist/enrollments_list.html', context)


def all_records(request):
    course_order = request.GET.get('course_order', 'name')
    student_order = request.GET.get('student_order', 'user__username')
    enrollment_order = request.GET.get('enrollment_order', 'date_enrolled')

    courses = Course.objects.all().order_by(course_order)
    students = Student.objects.all().order_by(student_order)
    enrollments = Enrollment.objects.all().order_by(enrollment_order)

    context = {
        'courses': courses,
        'students': students,
        'enrollments': enrollments
    }
    return render(request, 'degree_checklist/all_records.html', context)
