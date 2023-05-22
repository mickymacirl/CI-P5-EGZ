from django.shortcuts import render, redirect
from .forms import SubscriberForm
from .models import Subscriber


def subscribe(request):
    """
    This is a Python function that handles subscription requests,
    checks if the email already exists, and either saves the new
    subscriber or returns an error message.
    :param request: The request object represents the HTTP request
    that the user made to access the view
    :return: The code is defining two views for a newsletter
    subscription form.
    """
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            if Subscriber.objects.filter(email=email).exists():
                # email already exists, do something
                return render(
                    request, "newsletter/already_subscribed.html", {}
                    )
            else:
                subscriber = Subscriber.objects.create(email=email)
                subscriber.save()
                return render(request, "newsletter/success.html", {})
    else:
        form = SubscriberForm()
    return render(request, "newsletter/subscribe.html", {"form": form})


def already_subscribed(request):
    return render(request, "newsletter/already_subscribed.html", {})
