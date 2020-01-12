from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_requester        =       models.BooleanField('requester status', default=False)
    is_human_resource   =       models.BooleanField('Hr status', default=False)
    is_superviser       =       models.BooleanField('Superviser Status', default=False)
    is_autoriser        =       models.BooleanField('Autoriser Status', default=False)