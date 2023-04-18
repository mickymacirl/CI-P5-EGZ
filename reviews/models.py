from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class Rating(models.Model):
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='ratings')
#    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#    created_at = models.DateTimeField(auto_now_add=True)

#    class Meta:
#        unique_together = ('user', 'review')
