from django.db import models

# Create your models here.
class Contact(models.Model):
  contact_name = models.CharField(max_length=50)
  contact_phone = models.CharField(max_length=20)
  contact_email = models.CharField(max_length=50)
  contact_message = models.TextField(max_length=500)
  sent_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
        return self.contact_name

  class Meta:
      ordering = ['sent_at']
      verbose_name_plural = "Contacts"