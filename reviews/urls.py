from django.urls import path
from reviews.views import review_form, review_success, approved_reviews

urlpatterns = [
    path('', review_form, name='review_form'),
    path('success', review_success, name='review_success'),
    path('approved/', approved_reviews, name='approved_reviews'),
    #path('rate/', rate_review, name='rate_review'),
    #path('reviews/<int:pk>/rate/', rate_review, name='rate_review'),
    #path('reviews/<int:pk>/rate/', rate_review, name='rate_review'),
]