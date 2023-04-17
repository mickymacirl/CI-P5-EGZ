from django.shortcuts import render


# Create your views here.


def gdpr(request):
    """A view to return the contact us page"""

    return render(request, "gdpr/index.html")
