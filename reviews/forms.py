from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'review_text']
        labels = {
            'name': 'Your Name',
            'email': 'Email Address',
            'review_text': 'Review'
        }
