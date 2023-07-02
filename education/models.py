from django.db import models

# Create your models here.


class EducationType(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Education Types"
        
        
class Education(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(EducationType, max_length=50, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Education"
        