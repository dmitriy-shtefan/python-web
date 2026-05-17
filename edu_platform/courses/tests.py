from django.test import TestCase
from django.urls import reverse

from .forms import TeacherQuestionForm
from .models import Course


class CourseModelTests(TestCase):
    def test_course_str_returns_course_name(self):
        # Створюємо тестовий курс тільки в тимчасовій тестовій базі даних.
        course = Course.objects.create(
            name='Python Basics',
            description='Introductory Python course',
        )

        # Метод __str__ має повертати назву курсу, бо так курс показується в адмінці та формах.
        self.assertEqual(str(course), 'Python Basics')


class TeacherQuestionFormTests(TestCase):
    def test_question_with_three_question_marks_is_invalid(self):
        form = TeacherQuestionForm(data={
            'name': 'Student',
            'email': 'student@example.com',
            'question': 'Чому це не працює???',
        })

        # Форма повинна бути невалідною, бо clean_question забороняє "???" у питанні.
        self.assertFalse(form.is_valid())
        self.assertIn('question', form.errors)


class CoursesListViewTests(TestCase):
    def test_courses_list_page_shows_created_course(self):
        Course.objects.create(
            name='Django Basics',
            description='Introductory Django course',
        )

        # reverse знаходить URL за його name='courses_list', тому тест не залежить від конкретного шляху.
        response = self.client.get(reverse('courses_list'))

        # Перевіряємо, що сторінка відкрилась успішно і містить назву створеного курсу.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django Basics')
