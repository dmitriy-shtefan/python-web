from django.db import models


class Course(models.Model):
    LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200, null=True, blank=True)
    level = models.CharField(max_length=32, choices=LEVELS, default='beginner')
    price = models.DecimalField(decimal_places=2, max_digits=6, default=5000.0)
    is_test = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
