from django import forms
from .models import Review


# This is a Django form class for creating a
# review form with fields for name, email, and
# review text, and custom labels for each field.
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'review_text']
        labels = {
            'name': 'Your Name',
            'email': 'Email Address',
            'review_text': 'Review'
        }
