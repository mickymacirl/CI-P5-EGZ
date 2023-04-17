from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.subscribe, name="subscribe"),
    path("already-subscribed/", views.already_subscribed, name="already_subscribed"),
]
