from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html',
                  {'projects': projects,
                   'skills': skills}
    )

def projects(request, project_title):
    project = Project.objects.get(title=project_title)
    return render(request, 'project.html', {'project': project})