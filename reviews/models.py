from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


# This is a Django model for a review with fields for name,
# email, review text, approval status, and creation date.
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
