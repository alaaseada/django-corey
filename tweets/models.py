from django.db import models
from django.utils import timezone, timesince
from django.contrib.auth.models import User


class Tweet(models.Model):
    creation_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    last_modified= models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return self.content if len(self.content) <= 50 else self.content[:50]
