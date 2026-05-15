from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Course
from .models import Module
from .models import Enrollment

from .forms import TeacherQuestionForm
from .forms import EnrollmentForm
from .forms import CourseForm

from .permissions import is_teacher
from .permissions import is_student


# index
def index(request):
    return redirect('home')


# home view (CBV)
class HomeView(TemplateView):
    template_name = 'courses/home.html'


# about view
class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'courses/about.html'


# Class Based View
class CoursesListView(ListView):
    template_name = 'courses/courses_list.html'
    model = Course
    context_object_name = 'courses_list'


# Class Based View
class CourseDetailsView(DetailView):
    template_name = 'courses/course_details.html'
    model = Course
    context_object_name = 'course'


class ModulesListView(ListView):
    template_name = 'courses/modules_list.html'
    model = Module
    context_object_name = 'modules_list'


@login_required
def ask_question(request):
    if request.method == 'POST':
        form = TeacherQuestionForm(request.POST)
        if form.is_valid():
            return render(request, 'courses/question_sent.html', {'data': form.cleaned_data})
    else:
        form = TeacherQuestionForm()

    return render(request, 'courses/ask_question.html', {'form': form})


@login_required
@user_passes_test(is_student)
def enroll_course(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            exists = Enrollment.objects.filter(student=request.user, course=course, is_active=True).exists()

            if exists:
                form.add_error('course', 'Ви вже записані на цей курс')
            else:
                enrollment = form.save(commit=False)
                enrollment.student = request.user
                enrollment.save()
                messages.success(request=request, message='Ви успішно записалися на новий курс!')
                return redirect('my_courses')
    else:
        form = EnrollmentForm()

    return render(request, 'courses/enroll_course.html', {'form': form})


@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user).select_related('course')

    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})


@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    courses = Course.objects.filter(teacher=request.user).prefetch_related('enrollments', 'modules')

    return render(request, 'courses/teacher_dashboard.html', {'courses': courses})


@login_required
@user_passes_test(is_teacher)
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()

            messages.success(request, 'Курс було успішно створено!')
            return redirect('teacher_dashboard')
    else:
        form = CourseForm()

    return render(request,'courses/create_course.html', {'form': form})


def update_course(request):
    pass


def delete_course(request):
    pass
