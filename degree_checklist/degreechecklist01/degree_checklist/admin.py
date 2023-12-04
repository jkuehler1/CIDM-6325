from django.contrib import admin
from .models import Course, Student, Enrollment
from .forms import UploadFileForm


class CustomAdmin(admin.ModelAdmin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upload_form'] = UploadFileForm()
        return context


class CourseAdmin(CustomAdmin):
    change_form_template = 'admin/degree_checklist/course/change_form.html'
    list_display = ('code', 'name', 'credits')

class StudentAdmin(CustomAdmin):
    change_form_template = 'admin/degree_checklist/student/change_form.html'
    list_display = ('user',)

class EnrollmentAdmin(CustomAdmin):
    change_form_template = 'admin/degree_checklist/enrollment/change_form.html'
    list_display = ('student', 'course', 'date_enrolled', 'status')

if Course in admin.site._registry:
    admin.site.unregister(Course)
admin.site.register(Course, CourseAdmin)

if Student in admin.site._registry:
    admin.site.unregister(Student)
admin.site.register(Student, StudentAdmin)

if Enrollment in admin.site._registry:
    admin.site.unregister(Enrollment)
admin.site.register(Enrollment, EnrollmentAdmin)

