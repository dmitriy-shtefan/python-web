from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course
from .models import Module

from .forms import TeacherQuestionForm


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