from django.contrib import admin
from courses.models import Course
from courses.models import Module
from courses.models import Profile

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Profile)

