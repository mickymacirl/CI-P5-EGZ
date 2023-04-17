from django.contrib import admin
from django.urls import path
from .views import BlogView, BlogDetailView

urlpatterns = [
    #path('blog/', views.blog, name='blog')
    path('blog/', BlogView.as_view(), name="blog"),
    path('post/<int:pk>', BlogDetailView.as_view(), name="blog-detail"),
]