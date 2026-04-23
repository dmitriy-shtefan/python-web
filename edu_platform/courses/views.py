from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# home view
def home(request):
    http_method = request.method
    return HttpResponse(f"""<h1>Home Page!</h1>
                            <h3>HTTP Method: {http_method}</h3>
                        """)


# about view
def about(request):
    pass

def courses(request):
    pass