from django.db import models


class SignUp(models.Model):
    email = models.EmailField(max_length=254)
    date_signed_up = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email