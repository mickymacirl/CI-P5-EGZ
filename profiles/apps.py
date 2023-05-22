from django.apps import AppConfig


# This is a Django AppConfig class for the "profiles"
# app with a default auto field set to
# "django.db.models.BigAutoField".
class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
