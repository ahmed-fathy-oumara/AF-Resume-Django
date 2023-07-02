from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact


# Create your views here.


def contact(request):
  
    if request.method == 'POST':
        contact_name = request.POST['contact_name']
        contact_phone = request.POST['contact_phone']
        contact_email = request.POST['contact_email']
        contact_message = request.POST['contact_message']

        contact = Contact(contact_name=contact_name, contact_phone=contact_phone, contact_email=contact_email, contact_message=contact_message)

        contact.save()
        
        # Send Email
        send_mail(
            'New Contact Message',
            'You have received a new message from: ' + contact_name + 
            ', with phone number: ' + contact_phone + 
            ', and email: ' + contact_email + 
            '. The message content is: ' + contact_message,
            'dev.ahmed.85@gmail.com',
            ['ahmedfathyoumara@gmail.com'],
            fail_silently=False,
        )
        
        messages.success(request, 'Your message has been sent successfully .. Will get back to you shortly.')
        return redirect('home')