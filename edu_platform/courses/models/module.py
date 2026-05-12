from django.db import models

from . import Course


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules', null=True, blank=True)

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    number_of_classes = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
