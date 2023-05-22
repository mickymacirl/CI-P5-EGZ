from django.contrib import admin
from .models import Inquiry


# This is a Django admin model for managing inquiries
# with a list display, filters, and search fields.
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'subject',
        'created_at'
    )
    list_filter = ('created_at',)
    search_fields = ('full_name', 'email', 'subject', 'message')


admin.site.register(Inquiry, InquiryAdmin)
