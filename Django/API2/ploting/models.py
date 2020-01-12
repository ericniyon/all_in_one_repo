from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Poll(models.Model):
    question=models.CharField(max_length=200)
    ceated_by=models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question



class Choice(models.Model):
    poll=models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=255)


    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    choice= models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll=models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together=("poll", "voted_by")
    
    
class Article(models.Model):
    class Status:
        DRAFT = 0
        PUBLISHED = 1
        CHOICES = [(DRAFT, "Draft"), (PUBLISHED, "Published")]

    title = models.CharField(max_length=190)
    body = models.TextField()
    slug = models.SlugField(max_length=190)
    status = models.IntegerField(choices=Status.CHOICES, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class QuickReport():
        date_field = "created_at"