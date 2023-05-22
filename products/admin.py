from django.contrib import admin
from .models import Product, Category

# Register your models here.


# The `ProductAdmin` class defines the display and
# ordering options for a product model in the Django
# admin interface.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


# This is a Django admin model for displaying
# the friendly name and name of a category.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
