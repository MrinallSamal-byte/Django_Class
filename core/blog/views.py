# blog/views.py
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView

class PostListView(ListView):
    queryset = Post.published.all()
    template_name = 'blog/post/list.html'
    context_object_name = 'posts'
    paginate_by = 3
def post_list(request):
    posts = Post.published.all()
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3) 
    page_number = request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    posts = paginator.get_page(page_number)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_details(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, 'blog/post/details.html', {'post': post})