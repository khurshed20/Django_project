from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def mail_send(request) :
   send_mail(
    'Subject here : Django mail',
    'Here is the message : This is test mail from python Django Framework',
    'khurshedhasan71@gmail.com',
    ['khurshed_hasan@yahoo.com'],
    fail_silently=False,
)