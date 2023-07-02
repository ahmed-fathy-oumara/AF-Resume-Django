from django.contrib import admin
from .models import Profile, Resume, PersonalInfo, SocialLink

# Change the header title in Admin area
admin.site.site_header = 'AF RESUME'

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at')
  
class ResumeAdmin(admin.ModelAdmin):
  list_display = ('file_name', 'created_at')

class PersonalInfoAdmin(admin.ModelAdmin):
  list_display = ('gender', 'created_at')
   
class SocialLinkAdmin(admin.ModelAdmin):
  list_display = ('platform', 'link', 'created_at')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)