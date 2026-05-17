from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import TeacherQuestionForm
from .models import Course
from .models import Profile


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


class TeacherCourseCrudTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.teacher = user_model.objects.create_user(
            username='teacher1',
            password='password123',
        )
        self.other_teacher = user_model.objects.create_user(
            username='teacher2',
            password='password123',
        )

        Profile.objects.create(user=self.teacher, role=Profile.ROLE_TEACHER)
        Profile.objects.create(user=self.other_teacher, role=Profile.ROLE_TEACHER)

    def test_teacher_can_create_course_and_becomes_owner(self):
        self.client.login(username='teacher1', password='password123')

        response = self.client.get(reverse('course_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Створення курсу')

        response = self.client.post(reverse('course_create'), {
            'name': 'Teacher Course',
            'description': 'Created by teacher',
            'price': '1200.00',
            'level': 'beginner',
            'is_test': 'on',
        })

        self.assertRedirects(response, reverse('teacher_dashboard'))
        course = Course.objects.get(name='Teacher Course')
        self.assertEqual(course.teacher, self.teacher)
        self.assertTrue(course.is_test)

    def test_teacher_can_update_only_own_course(self):
        own_course = Course.objects.create(
            name='Own Course',
            description='Initial',
            teacher=self.teacher,
        )
        other_course = Course.objects.create(
            name='Other Course',
            description='Initial',
            teacher=self.other_teacher,
        )
        self.client.login(username='teacher1', password='password123')

        response = self.client.get(reverse('course_update', args=[own_course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Редагування курсу')

        response = self.client.post(reverse('course_update', args=[own_course.id]), {
            'name': 'Updated Course',
            'description': 'Updated',
            'price': '5000.00',
            'level': 'intermediate',
        })

        self.assertRedirects(response, reverse('teacher_dashboard'))
        own_course.refresh_from_db()
        self.assertEqual(own_course.name, 'Updated Course')
        self.assertEqual(own_course.level, 'intermediate')

        response = self.client.get(reverse('course_update', args=[other_course.id]))
        self.assertEqual(response.status_code, 404)

    def test_teacher_can_delete_only_own_course_with_post(self):
        own_course = Course.objects.create(
            name='Own Course',
            description='Initial',
            teacher=self.teacher,
        )
        other_course = Course.objects.create(
            name='Other Course',
            description='Initial',
            teacher=self.other_teacher,
        )
        self.client.login(username='teacher1', password='password123')

        response = self.client.get(reverse('course_delete', args=[own_course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Course.objects.filter(id=own_course.id).exists())

        response = self.client.post(reverse('course_delete', args=[own_course.id]))
        self.assertRedirects(response, reverse('teacher_dashboard'))
        self.assertFalse(Course.objects.filter(id=own_course.id).exists())

        response = self.client.post(reverse('course_delete', args=[other_course.id]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Course.objects.filter(id=other_course.id).exists())
