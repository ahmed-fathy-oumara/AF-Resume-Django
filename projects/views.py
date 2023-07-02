from django.shortcuts import render
from .models import Project
from profiles.models import Resume

# Create your views here.

def projects(request):
    # Resume Files
    my_resumes = Resume.objects.all()
    
    projects_list = Project.objects.all()
    
    context = {
        'my_resumes': my_resumes,
        'projects_list': projects_list,
    }
    return render(request, 'pages/projects.html', context)