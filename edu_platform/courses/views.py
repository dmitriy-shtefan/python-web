from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


from .models import Course


# index
def index(request):
    return redirect('home')


# home view
def home(request):

    return render(request, 'courses/home.html')


# about view
def about(request):

    return render(request, 'courses/about.html')

# courses_list view
def courses_list(request):
    courses = Course.objects.all()

    context = {'courses_list': courses}

    return render(request, 'courses/courses_list.html', context)


# courses view
def course_details(request, course_id):
    # класичний спосіб, але потрібно обробляти винятки
    # course = Course.objects.get(pk=course_id)

    course = get_object_or_404(Course, pk=course_id)

    context = {'course': course}

    return render(request, 'courses/course_details.html', context)


def modules(request):
    modules_list = get_modules_list()
    context = {'modules_list': modules_list}

    return render(request, 'courses/modules_list.html', context)


def get_courses_list() -> list:
    return [
        {
            "id": 1,
            "name": "Об’єктно-орієнтоване програмування (C++)",
            "description": "Вивчення класів, об'єктів, наслідування та основ ООП на мові C++."
        },
        {
            "id": 2,
            "name": "Теорія баз даних",
            "description": "Основи роботи з базами даних, SQL-запити та проєктування таблиць."
        },
        {
            "id": 3,
            "name": "Web (HTML + CSS)",
            "description": "Створення веб-сторінок за допомогою HTML та стилізація з CSS."
        },
        {
            "id": 4,
            "name": "Розробка веб-додатків на Python",
            "description": "Створення серверної логіки веб-додатків на Python (Django), робота з базами даних та обробка HTTP-запитів."
        },
    ]

def get_modules_list() -> list:
    return [
        {"name": "Django: Setup",            "number_of_classes": 2},
        {"name": "Django: Templates",        "number_of_classes": 4},
        {"name": "Django: Models",           "number_of_classes": 6},
        {"name": "Django: Views",            "number_of_classes": 5},
        {"name": "Django: URLs",             "number_of_classes": 3},
        {"name": "Django: Forms",            "number_of_classes": 4},
        {"name": "Django: Admin",            "number_of_classes": 2},
        {"name": "Django: Authentication",   "number_of_classes": 5},
        {"name": "Django: ORM Advanced",     "number_of_classes": 6},
        {"name": "Django: REST API",         "number_of_classes": 7},
        {"name": "Django: Testing",          "number_of_classes": 3},
    ]