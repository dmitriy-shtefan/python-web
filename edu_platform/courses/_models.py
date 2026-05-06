# Переіменований файл з моделями. Основні моделі зберігаються в /models

from django.db import models


class Course(models.Model):
    LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    level = models.CharField(max_length=32, choices=LEVELS, default='beginner')
    is_test = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Module(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    number_of_classes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
