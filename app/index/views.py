from django.shortcuts import render
from .models import Task, Slide


def index(request):
    tasks = Task.objects.all()
    slide = Slide.objects.all()
    contex = {
        'tasks': tasks,
        'slide': slide[0]  
        }
    return render(request, 'page/content.html', contex)


def about(request):
    return render(request, 'page/about.html')


def contakt(request):
    return render(request, 'page/contakt.html')