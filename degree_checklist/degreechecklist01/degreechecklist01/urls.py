"""
URL configuration for degreechecklist01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from degree_checklist import views
from degree_checklist.views import upload_file
from django.conf import settings
from django.conf.urls.static import static



if settings.DEBUG:
    import debug_toolbar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.list_courses, name='list_courses'),
    path('students/', views.list_students, name='list_students'),
    path('enrollments/', views.list_enrollments, name='list_enrollments'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_enrollment/', views.add_enrollment, name='add_enrollment'),
    path('', views.all_records, name='all_records'),
    path('upload/', upload_file, name='upload_file'),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


