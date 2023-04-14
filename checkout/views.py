from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "The cart is empty! Please add products!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MvLtwA0gI4jFgzQlDLpfEKj0xUp5F0NREBsV551LtaP6czbyJZjAh1TayG85C04nfBN57p0iMSV78OeIyY5REZU00Ym0h1HDY',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
