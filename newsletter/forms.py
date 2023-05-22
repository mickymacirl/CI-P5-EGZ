from django import forms


# This is a Python class for a subscriber form that
# includes an email field with a label, required
# attribute, and widget for user input.
class SubscriberForm(forms.Form):
    email = forms.EmailField(
        label="Enter your email address",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "youremail@example.com",
            }
        ),
    )
