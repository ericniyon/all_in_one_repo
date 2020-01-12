from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confrm_message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        comments = form.cleaned_data['comments']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comments, name)
        email_from = form.cleaned_data['email']
        email_to = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,email_from, email_to, fail_silently=False,)
        title = 'Thanks'
        confrm_message= 'Thanks for mailing me .'
        form = None
    context = {'title': title, 'form': form, 'confrm_message':confrm_message}

   
    template = 'contact.html'
    return render(request, template, context)

#desplaying contact view list
class ContactList(ListView): 
    model = Contact
#detailing contact view list
class ContactDetail(DetailView): 
    model = Contact
#creating contact view list
class ContactCreate(CreateView): 
    model = Contact
#updating contact view list
class ContactUpdate(UpdateView): 
    model = Contact
    fields=['name','email','address','phone']
#delting contact view list
class ContactDelete(DeleteView): 
    model = Contact