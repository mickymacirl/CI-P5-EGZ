from django.db import models
import datetime


# The Subscriber class defines a model with an email field.
class Subscriber(models.Model):
    email = models.EmailField(default="")

    def __str__(self):
        return self.email
