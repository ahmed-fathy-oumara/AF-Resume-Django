from django.shortcuts import render
from .models import Education
from profiles.models import Resume

# Create your views here.

def education(request):
    # Resume Files
    my_resumes = Resume.objects.all()
    
    certificate_degrees = Education.objects.filter(type__name__iexact='Certificate Degree')
    certificates_list = list(certificate_degrees)
    certificates_list1 = certificates_list[0:6]
    certificates_list2 = certificates_list[6:12]
    bachelor_degrees = Education.objects.filter(type__name__iexact='Bachelor Degree')
    school_degrees = Education.objects.filter(type__name__iexact='School Degree')
    
    context = {
        'my_resumes': my_resumes,
        'certificate_degrees': certificate_degrees,
        'certificates_list1': certificates_list1,
        'certificates_list2': certificates_list2,
        'bachelor_degrees': bachelor_degrees,
        'school_degrees': school_degrees,
    }
    return render(request, 'pages/education.html', context)