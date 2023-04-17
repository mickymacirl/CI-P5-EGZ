from django.shortcuts import render


# Create your views here.


def ethical(request):
    """A view to return the contact us page"""

    return render(request, "ethical/index.html")
