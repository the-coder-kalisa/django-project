from django.http import HttpResponse
from .models import Tasks


def index(request):
    tasks = Tasks.objects.all()
    return HttpResponse(len(tasks)) 


def add_task(request):
    return HttpResponse("<h1>hello</h1>")
