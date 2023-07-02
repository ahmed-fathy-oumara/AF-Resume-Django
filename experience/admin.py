from django.contrib import admin
from .models import Employer, Job, JobDescription

# Register your models here.

class EmployerAdmin(admin.ModelAdmin):
  list_display = ('name', 'last_job_title', 'type', 'contract', 'created_at')
  
class JobAdmin(admin.ModelAdmin):
  list_display = ('title', 'company', 'created_at')
  
class JobDescriptionAdmin(admin.ModelAdmin):
  list_display = ('title', 'job', 'created_at')
  
  
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobDescription, JobDescriptionAdmin)