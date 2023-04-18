from django import forms
from .models import Inquiry


# The `InquiryForm` class is a model form that
# includes fields for `full_name`, `email`,
# `phone_number`, `subject`, and `message` from
# the `Inquiry` model.
class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']
