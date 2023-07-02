from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    job_title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
      
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Profiles"


class Resume(models.Model):
    file_name = models.CharField(max_length=50)
    cv_file = models.FileField(blank=True, upload_to='resumes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
      
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Resumes"

class PersonalInfo(models.Model):
    summary = models.TextField(max_length=1000)
    gender = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    birthdate = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=50)
    marital_status = models.EmailField(max_length=50)
    military_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gender

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Personal Info"


class SocialLink(models.Model):
    PLATFORMS = (
        ('Facebook', 'Facebook'),
        ('LinkedIn', 'LinkedIn'),
        ('Twitter', 'Twitter'),
        ('Discord', 'Discord'),
        ('Whatsapp', 'Whatsapp'),
        ('Telegram', 'Telegram'),
        ('Messanger', 'Messanger'),
        ('Instagram', 'Instagram'),
    )
    user_profile = models.ForeignKey(Profile, max_length=50,on_delete=models.CASCADE, null=True)
    platform = models.CharField(max_length=50, choices=PLATFORMS, default='Facebook')
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.platform

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Social Links"