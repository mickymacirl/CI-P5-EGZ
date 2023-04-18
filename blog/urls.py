from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import BlogView, BlogDetailView, like_post, AddPostView, UpdatePostView
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('blog/', views.blog, name='blog')
    path("blog/", BlogView.as_view(), name="blog"),
    path("post/<int:pk>", BlogDetailView.as_view(), name="blog-detail"),
    path("post/<int:pk>/like/", like_post, name="like_post"),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    #path("login/", LoginView.as_view(), name="login"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("post/edit_post/<int:pk>", UpdatePostView.as_view(), name="update_post"),
]
