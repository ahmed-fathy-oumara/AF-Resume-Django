from django.shortcuts import render
from .models import Resume
from projects.models import Project
from skills.models import Skill
from education.models import Education

# Create your views here.

def home(request):
    # Resume Files
    my_resumes = Resume.objects.all()
  
    # Projects Views
    projects_list = Project.objects.all()
    
    # Skills Views
    frontend_skills = Skill.objects.filter(type__name__iexact='Frontend Skills')
    frontend_skills_list = list(frontend_skills)
    frontend_skills_list1 = frontend_skills_list[0:9]
    frontend_skills_list2 = frontend_skills_list[9:18]
    backend_skills = Skill.objects.filter(type__name__iexact='Backend Skills')
    backend_skills_list = list(backend_skills)
    backend_skills_list1 = backend_skills_list[0:3]
    backend_skills_list2 = backend_skills_list[3:6]
    tooling_skills = Skill.objects.filter(type__name__iexact='Tooling Skills')
    tooling_skills_list = list(tooling_skills)
    tooling_skills_list1 = tooling_skills_list[0:6]
    tooling_skills_list2 = tooling_skills_list[6:12]
    language_skills = Skill.objects.filter(type__name__iexact='Language Skills')
    language_skills_list = list(language_skills)
    language_skills_list1 = language_skills_list[0:2]
    language_skills_list2 = language_skills_list[2:4]
    personal_skills = Skill.objects.filter(type__name__iexact='Personal Skills')
    
    # Education Views
    certificate_degrees = Education.objects.filter(type__name__iexact='Certificate Degree')
    certificates_list = list(certificate_degrees)
    certificates_list1 = certificates_list[0:6]
    certificates_list2 = certificates_list[6:12]
    bachelor_degrees = Education.objects.filter(type__name__iexact='Bachelor Degree')
    school_degrees = Education.objects.filter(type__name__iexact='School Degree')
    
    context = {
        'my_resumes': my_resumes,
        'projects_list': projects_list,
        'frontend_skills': frontend_skills,
        'frontend_skills_list1': frontend_skills_list1,
        'frontend_skills_list2': frontend_skills_list2,
        'backend_skills': backend_skills,
        'backend_skills_list1': backend_skills_list1,
        'backend_skills_list2': backend_skills_list2,
        'tooling_skills': tooling_skills,
        'tooling_skills_list1': tooling_skills_list1,
        'tooling_skills_list2': tooling_skills_list2,
        'language_skills': language_skills,
        'language_skills_list1': language_skills_list1,
        'language_skills_list2': language_skills_list2,
        'personal_skills': personal_skills,
        'certificate_degrees': certificate_degrees,
        'certificates_list1': certificates_list1,
        'certificates_list2': certificates_list2,
        'bachelor_degrees': bachelor_degrees,
        'school_degrees': school_degrees,
    }
    return render(request, 'pages/home.html', context)
