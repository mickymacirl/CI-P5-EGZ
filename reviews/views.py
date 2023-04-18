from django.shortcuts import render, redirect
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
    context = {'reviews': reviews}
    return render(request, 'reviews/approved_reviews.html', context)