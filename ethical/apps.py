from django.apps import AppConfig


# This is a Django AppConfig class for the "ethical" app
# with a default auto field set to
# "BigAutoField".
class EthicalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ethical"
