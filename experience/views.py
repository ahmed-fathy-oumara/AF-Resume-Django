from django.shortcuts import render
from .models import Employer, Job, JobDescription
from profiles.models import Resume

# Create your views here.

def experience(request):
    # Resume Files
    my_resumes = Resume.objects.all()
    
    employers_list = Employer.objects.all()
    jobs_list = Job.objects.filter(company__name__iexact='company')
    
    senior_frontend_job_description = JobDescription.objects.filter(job__title__iexact='Senior Frontend Developer')
    frontend_job_description = JobDescription.objects.filter(job__title__iexact='Frontend Developer')
    designer_job_description = JobDescription.objects.filter(job__title__iexact='UI/UX Designer')
    partnership_manager_job_description = JobDescription.objects.filter(job__title__iexact='Partnership Manager')
    business_acquisition_job_description = JobDescription.objects.filter(job__title__iexact='Business Acquisition Teamleader')
    senior_compensation_benefits_job_description = JobDescription.objects.filter(job__title__iexact='Senior Compensation & Benefits Specialist')
    compensation_benefits_job_description = JobDescription.objects.filter(job__title__iexact='Compensation & Benefits Specialist')
    customer_service_agent_job_description = JobDescription.objects.filter(job__title__iexact='First-class Customer Service Agent')
    telesales_agent_job_description = JobDescription.objects.filter(job__title__iexact='Tele-Sales Agent')
    
    
    context = {
        'my_resumes': my_resumes,
        'employers_list': employers_list,
        'jobs_list': jobs_list,
        'senior_frontend_job_description': senior_frontend_job_description,
        'frontend_job_description': frontend_job_description,
        'designer_job_description': designer_job_description,
        'partnership_manager_job_description': partnership_manager_job_description,
        'business_acquisition_job_description': business_acquisition_job_description,
        'senior_compensation_benefits_job_description': senior_compensation_benefits_job_description,
        'compensation_benefits_job_description': compensation_benefits_job_description,
        'customer_service_agent_job_description': customer_service_agent_job_description,
        'telesales_agent_job_description': telesales_agent_job_description,
    }
    return render(request, 'pages/experience.html', context)