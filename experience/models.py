from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Employer(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(blank=True, upload_to='employers/logos')
    last_job_title = models.CharField(max_length=100)
    multi_jobs = models.BooleanField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=50)
    contract = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    start_end_date = models.CharField(max_length=50, null=True)
    years_of_experience = models.CharField(max_length=10)
    collapse_id = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Employers"


class Job(models.Model):
    company = models.ForeignKey(Employer, max_length=50, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    start_end_date = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Jobs"
        
        
class JobDescription(models.Model):
    title = models.CharField(max_length=100, null=True)
    job = models.ForeignKey(Job, max_length=50, on_delete=models.CASCADE)
    description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Job Descriptions"