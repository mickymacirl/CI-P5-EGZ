import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    # `order_number` is a field in the `Order` model that is a character field
    # with a maximum length
    # of 32 characters. It cannot be null and is not editable. It is used to
    # store a unique identifier
    # for each order, generated using the `_generate_order_number` method.
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    # `grand_total` is a DecimalField in the `Order` model with a maximum of
    # 10 digits and 2 decimal
    # places. It cannot be null and has a default value of 0. This field
    # represents the total cost of
    # an order, including the order total and any delivery costs. It is
    # updated each time a line item
    # is added to the order using the `update_total` method.
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_cart = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=""
        )

    def _generate_order_number(self):
        """
        return uuid.uuid4().hex.upper()` is generating a random, unique
        order number using UUID
        (Universally Unique Identifier) and converting it to a hexadecimal
        string in uppercase format.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        # This code is updating the total cost of an order (`self.grand_total`)
        #  by calculating the sum of all
        # line item totals (`self.order_total`) and adding the delivery cost
        # (`self.delivery_cost`). If the
        # order total is less than the free delivery threshold specified in
        # the settings, the delivery cost is
        # calculated as a percentage of the order total using the
        # `STANDARD_DELIVERY_PERCENTAGE` setting.
        # Otherwise, the delivery cost is set to 0. Finally, the updated
        # `grand_total` is saved to the
        # database.
        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))["lineitem_total__sum"] or 0
        )
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    product_size = models.CharField(
        max_length=2, null=True, blank=True
    )  # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        This function overrides the original save method to set the lineitem
        total and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        This function returns a string representation of an order with its
        associated product SKU.
        :return: The `__str__` method is returning a string that includes the
        SKU of a product and the order number it is associated with. The
        format of the string is "SKU {product_sku} on order
        {order_number}".
        """
        return f"SKU {self.product.sku} on order {self.order.order_number}"
