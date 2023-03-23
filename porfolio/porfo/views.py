from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html',
                  {'projects': projects})
