from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.urls import reverse


# This is a Django model class for a blog post with fields for title, author,
# body, and creation date.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    # likes
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} | {self.author.username}"

    def get_absolute_url(self):
        return reverse('blog-detail', args=(str(self.id),))
