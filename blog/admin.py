from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_on")
    list_filter = ("author", ("created_on", DateFieldListFilter))
    actions = ["delete_all_posts"]
    ordering = ("title",)

    def delete_all_posts(self, request, queryset):
        queryset.delete()

    delete_all_posts.short_description = "Delete All Posts"


admin.site.register(Post, PostAdmin)
