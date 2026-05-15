"""
URL configuration for edu_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.urls import path

from .views import HomeView
from .views import AboutView
from .views import CoursesListView
from .views import CourseDetailsView
from .views import ModulesListView
from .views import ask_question
from .views import enroll_course
from .views import my_courses
from .views import teacher_dashboard
from .views import create_course
from .views import update_course
from .views import delete_course

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('courses/list/', CoursesListView.as_view(), name='courses_list'),
    path('courses/<int:pk>/', CourseDetailsView.as_view(), name='course_details'),
    path('courses/create/', create_course, name='create_course'),
    path('courses/<int:pk>/update/', update_course, name='update_course'),
    path('courses/<int:pk>/delete/', delete_course, name='delete_course'),
    path('modules/list/', ModulesListView.as_view(), name='modules_list'),
    path('ask-question/', ask_question, name='ask_question'),
    path('my-courses/', my_courses, name='my_courses'),
    path('enroll-course/', enroll_course, name='enroll_course'),
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard')
]
