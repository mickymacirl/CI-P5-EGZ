from django.contrib import admin
from .models import Review

# This is a Django admin class that displays a list
# of reviews with their name, email, and creation
# date, and allows for the approval of selected reviews.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Review, ReviewAdmin)
