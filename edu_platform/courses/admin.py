from django.contrib import admin
from courses.models import Course
from courses.models import Module
from courses.models import Profile
from courses.models import Enrollment

admin.site.register(Profile)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['course__name', 'student__username']
    list_filter = []
