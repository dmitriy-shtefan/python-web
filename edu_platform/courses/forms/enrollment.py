from django import forms

from ..models import Course
from ..models import Enrollment


class EnrollmentForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user is not None:
            self.fields["course"].queryset = Course.objects.exclude(
                enrollments__student=user,
                enrollments__is_active=True,
            )

    class Meta:
        model = Enrollment
        fields = ['course']

        labels = {
            'course': 'Курс'
        }
