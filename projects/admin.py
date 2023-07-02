from django.contrib import admin
from .models import Project, ProjectCategory

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('title', 'category', 'created_at')
  
class ProjectCategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at')


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)