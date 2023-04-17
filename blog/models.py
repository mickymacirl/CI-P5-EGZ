from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


# This is a Django model class for a blog post with fields for title, author, body, and creation date.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

#    def __str__(self):
#        return self.title + '|' + self.author
    def __str__(self):
        return f"{self.title} | {self.author.username}"
