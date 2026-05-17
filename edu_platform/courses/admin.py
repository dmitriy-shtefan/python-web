from django.contrib import admin
from courses.models import Course
from courses.models import Module
from courses.models import Profile
from courses.models import Enrollment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    list_filter = ['role']
    search_fields = ['user__username', 'user__email']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'level', 'is_test']
    list_filter = ['level', 'is_test', 'teacher']
    search_fields = ['name', 'description', 'teacher__username']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'order', 'number_of_classes']
    list_filter = ['course']
    search_fields = ['name', 'course__name']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'is_active', 'created_at']
    list_filter = ['is_active', 'course']
    search_fields = ['student__username', 'course__name']
