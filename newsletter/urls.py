from django.contrib import admin
from django.urls import path
from . import views

# This code is defining the URL patterns for a Django web application.
urlpatterns = [
    path("", views.subscribe, name="subscribe"),
    path("already-subscribed/", views.already_subscribed,
         name="already_subscribed"),
]
