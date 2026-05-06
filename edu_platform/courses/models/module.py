from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    number_of_classes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
