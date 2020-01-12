from django.db import models
from dashboad.models import SchoolModel
from django.contrib.auth.models import AbstractUser
from django.urls import reverse



class User(AbstractUser):
    is_requester        =       models.BooleanField('requester status', default=False)
    is_human_resource   =       models.BooleanField('Hr status', default=False)
    is_superviser       =       models.BooleanField('Superviser Status', default=False)
    is_autoriser        =       models.BooleanField('Autoriser Status', default=False)
    school              =       models.ForeignKey(SchoolModel, on_delete=models.CASCADE,null=True, blank=True)
    profile_img         =       models.ImageField(upload_to='img', null=True, blank=True,default='/media/static/images/profile.png')

    def get_absolute_url(self):
        return reverse('account')