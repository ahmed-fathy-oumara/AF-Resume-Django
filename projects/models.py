from django.db import models

# Create your models here.

class ProjectCategory(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Project Categories"
        

class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ProjectCategory, max_length=50, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    large_image = models.ImageField(blank=True, upload_to='projects/largeimages')
    small_image = models.ImageField(blank=True, upload_to='projects/smallimages')
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Projects"