from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200, blank=True, null=True)
    is_test = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
