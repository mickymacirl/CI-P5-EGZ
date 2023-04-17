from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Post

# Create your views here.


# def blog(request):
#    """ A view to return the index page """
#
#    return render(request, 'blog/index.html')
# This is a class-based view for displaying a list of posts in descending order of creation time on a
# blog index page.


class BlogView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-created_on"]

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['like_post_url'] = reverse('like_post', kwargs={'pk': 1})  # replace `1` with a valid Post pk value
    #    print('like_post_url:', context['like_post_url'])
    #    return context


# This is a Django class-based view for displaying the details of a blog post using a specific
# template.
class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_details.html"


# @login_required
# def like_post(request, pk):
#    print('pk:', pk)
#    post = Post.objects.get(pk=pk)
#    post.likes += 1
#    post.save()
#    messages.success(request, f"You liked {post.title}!")
#    return redirect('post_details', pk=post.pk)


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
