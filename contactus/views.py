from django.shortcuts import render


# Create your views here.


def contactus(request):
    """A view to return the contact us page"""

    return render(request, "contactus/index.html")
