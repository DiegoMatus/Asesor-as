from django.shortcuts import render, render_to_response
from .models import Student, Project

# Create your views here.
def index(request):
	projects = Project.objects.all()
	context = {'projects': projects}
	return render(request, 'coafid/index.html', context)

def student_view(request, student_slug):
	return render(request, 'coafid/student.html')

def project_view(request, project_slug):
	project = Project.objects.get(slug = project_slug)
	context = {'project': project}
	return render(request, 'coafid/project.html', context)

def advisory_view(request, student):
	return render(request, 'coafid/advisory.html')