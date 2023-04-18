from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review

def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_success')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

def review_success(request):
    return render(request, 'reviews/review_success.html')

def approved_reviews(request):
    reviews = Review.objects.filter(approved=True)
    return render(request, 'reviews/approved_reviews.html', {'reviews': reviews})

#@login_required
#def rate_review(request, pk):
#    review = Review.objects.get(pk=pk)
#    if request.method == 'POST':
#        form = RatingForm(request.POST)
#        if form.is_valid():
#            rating = form.save(commit=False)
#            rating.user = request.user
#            rating.review = review
#            rating.save()
#            return redirect('review_success')
#    else:
#        form = RatingForm()
#    return render(request, 'reviews/rate_review.html', {'form': form, 'review': review})
