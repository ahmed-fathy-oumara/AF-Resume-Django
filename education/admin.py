from django.contrib import admin
from .models import EducationType, Education

# Register your models here.

class EducationTypeAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at')
  
class EducationAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'created_at')

admin.site.register(EducationType, EducationTypeAdmin)
admin.site.register(Education, EducationAdmin)