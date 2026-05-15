from django.db import models
from django.conf import settings


class Profile(models.Model):
    ROLE_TEACHER = 'teacher'
    ROLE_STUDENT = 'student'

    ROLES = [
        (ROLE_TEACHER, 'teacher'),
        (ROLE_STUDENT, 'student')
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    role = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.user.username