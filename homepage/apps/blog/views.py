# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class BlogListView(ListView):
    template_name = "blog/index.html"
    queryset = Post.objects.order_by('-created')[:6]

class PostDetailView(DetailView):
    template_name="blog/post-details.html"
    model=Post

def index(request):
    return render(request, "blog/index.html", {"object_list":Post.objects.order_by('-created')[:6]})

def test_view(request):
    pass
