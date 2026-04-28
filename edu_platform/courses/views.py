from django.shortcuts import render

# home view
def home(request):

    return render(request, 'courses/home.html')


# about view
def about(request):

    return render(request, 'courses/about.html')

# courses_list view
def courses_list(request):
    context = {'courses_list': get_courses_list()}

    return render(request, 'courses/courses_list.html', context)


# courses view
def course_details(request, course_id):
    courses_list = get_courses_list()

    course = None
    for c in courses_list:
        if c['id'] == course_id:
            course = c

    context = {'course': course}

    return render(request, 'courses/course_details.html', context)

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