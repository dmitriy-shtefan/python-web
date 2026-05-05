# Переіменований файл з моделями. Основні моделі зберігаються в /models

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    is_test = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Module(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
