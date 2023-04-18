from django.contrib import admin
from .models import Inquiry

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'email', 'subject', 'message')

admin.site.register(Inquiry, InquiryAdmin)