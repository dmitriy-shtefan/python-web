from django.shortcuts import render

# home view
def home(request):

    return render(request, 'courses/home.html')


# about view
def about(request):

    return render(request, 'courses/about.html')


# courses view
def course_details(request, course_id):

    return render(request, 'courses/course_details.html', {'course_id': course_id})