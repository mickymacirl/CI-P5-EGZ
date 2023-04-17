from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


#def blog(request):
#    """ A view to return the index page """
#
#    return render(request, 'blog/index.html')
# This is a class-based view for displaying a list of posts in descending order of creation time on a
# blog index page.

class BlogView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-created_on']

# This is a Django class-based view for displaying the details of a blog post using a specific
# template.
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'