from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Post


class BlogView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-created_on"]

# This is a Django class-based view for displaying the details of a blog post
# using a specific template.


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_details.html"


@csrf_exempt
@require_POST
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse("blog-detail", args=[pk]))


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["like_post_url"] = reverse("like_post", kwargs={"pk": 1})
    return context


class AddPostView(UserPassesTestMixin, CreateView):
    model = Post
    template_name = "blog/add_post.html"
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_superuser


class UpdatePostView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_superuser


class DeletePostView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('blog')

    def test_func(self):
        return self.request.user.is_superuser
