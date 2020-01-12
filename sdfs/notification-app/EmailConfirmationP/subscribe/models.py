from django.db import models
from EmailConfirmationP.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db.models.signals import post_save




class Post(models.Model):
    title           = models.CharField(max_length=200)
    description     = models.TextField()
    published       = models.BooleanField(default=True)
    published_date  = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title


def save_article(sender, instance,**kwargs):

    subject = "Welcome User"
    message = 'New Post is added successfully !!!'
    recepient = 'iradukunda.ta@gmail.com'
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)


post_save.connect(save_article, sender=Post)




