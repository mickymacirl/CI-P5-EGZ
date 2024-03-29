from django.db import models

# This is a Django model for an inquiry form that
# includes fields for full name, email, phone number,
# subject, message, and creation date.


class Inquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
