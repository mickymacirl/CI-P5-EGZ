from django.shortcuts import render


# Create your views here.


def tad(request):
    """ A view to return the contact us page """

    return render(request, 'tad/index.html')