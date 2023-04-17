from django import forms


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
