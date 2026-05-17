from django import forms
from ..models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'price', 'level', 'is_test']

        labels = {
            'name': 'Назва Курсу',
            'description': 'Опис Курсу',
            'price': 'Ціна',
            'level': 'Рівень',
            'is_test': 'Тестовий курс',
        }

        widgets = {
            'description': forms.Textarea(attrs={'class': 'course-description'})
        }
