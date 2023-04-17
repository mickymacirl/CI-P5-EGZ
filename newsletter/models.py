from django.db import models
import datetime

class Subscriber(models.Model):
    email = models.EmailField(default='')

    def __str__(self):
        return self.email