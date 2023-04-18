from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    search_fields = ('name', 'email', 'comment')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at')
