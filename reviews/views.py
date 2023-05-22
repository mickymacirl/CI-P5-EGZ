from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review


def review_form(request):
    """
    This function handles the submission of a review form and saves the data
    if it is valid.
    :param request: The request object represents the HTTP request that the
    user made to access the view. the function saves the form and redirects
    to the `review_success` URL.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_success')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})


def review_success(request):
    """
    The function returns a rendered HTML template for a successful review
    submission.
    :param request: The request parameter is an object that represents the
     HTTP request made by the client to the server. It contains
     information about the request, such as the URL, headers, and any
    data sent in the request body. In this code snippet, the request
    parameter is used to render the 'review_success.html'
    :return: an HTTP response that renders the 'review_success.html' template.
    """
    return render(request, 'reviews/review_success.html')


def approved_reviews(request):
    """
    This function retrieves all approved reviews and renders
    them in a template.
    :param request: The request parameter is an object that represents the
    HTTP request made by the client to the server. It contains information
    such as the HTTP method used (GET, POST, etc.), the
    """
    reviews = Review.objects.filter(approved=True)
    return render(
        request, 'reviews/approved_reviews.html', {'reviews': reviews}
        )
