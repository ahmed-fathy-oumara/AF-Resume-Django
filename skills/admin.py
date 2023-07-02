from django.contrib import admin
from .models import SkillType, Skill

# Register your models here.

class SkillTypeAdmin(admin.ModelAdmin):
  list_display = ('name', 'created_at')
  
class SkillAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'created_at')


admin.site.register(SkillType, SkillTypeAdmin)
admin.site.register(Skill, SkillAdmin)