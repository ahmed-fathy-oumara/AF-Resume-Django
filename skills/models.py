from django.db import models

# Create your models here.

class SkillType(models.Model):

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Skills Types"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(SkillType, max_length=50, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Skills"
