from django.apps import AppConfig


# This is a Django AppConfig class for the "newsletter" app
# with a default auto field set to
# "django.db.models.BigAutoField".
class NewsletterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "newsletter"
