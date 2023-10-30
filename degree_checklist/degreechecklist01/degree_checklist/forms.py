from django import forms
from .models import Course, Student, Enrollment


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'


class UploadFileForm(forms.Form):
    file = forms.FileField()
