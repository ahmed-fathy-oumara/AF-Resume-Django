from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
  list_display = ('contact_name', 'contact_phone', 'contact_email', 'sent_at')

admin.site.register(Contact, ContactAdmin)