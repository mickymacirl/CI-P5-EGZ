from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    # `instance.order.update_total()` is calling the `update_total()` method on the `order` object
    # associated with the `OrderLineItem` instance. This method is likely defined in the `Order` model
    # and is responsible for recalculating the total cost of the order based on the current state of
    # its associated line items.
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    # `instance.order.update_total()` is calling the `update_total()` method on the `order` object
    # associated with the `OrderLineItem` instance. This method is likely defined in the `Order` model
    # and is responsible for recalculating the total cost of the order based on the current state of
    # its associated line items. So, it updates the total cost of the order whenever a new
    # `OrderLineItem` is created or an existing one is updated or deleted.
    instance.order.update_total()
