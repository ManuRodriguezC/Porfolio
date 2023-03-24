from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html',
                  {'projects': projects,
                   'skills': skills}
    )

def projects(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project.html', {'project': project})