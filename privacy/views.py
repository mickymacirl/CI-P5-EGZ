from django.shortcuts import render


# Create your views here.


def privacy(request):
    """A view to return the privacy page"""

    return render(request, "privacy/index.html")
