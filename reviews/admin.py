from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)

#@admin.register(Rating)
#class RatingAdmin(admin.ModelAdmin):
#    list_display = ['user', 'review', 'value', 'created_at']
#    search_fields = ['user__username', 'review__name']
#    ordering = ['-created_at']

admin.site.register(Review, ReviewAdmin)
