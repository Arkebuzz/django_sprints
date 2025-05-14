from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def get_all_posts():
    posts = Post.objects.select_related(
        'location', 'author', 'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    return posts


def index(request):
    template_name = 'blog/index.html'
    posts = get_all_posts()[:5]
    context = {'post_list': posts}
    return render(request, template_name, context)


def post_detail(request, post_id):
    posts = get_all_posts()
    post = get_object_or_404(posts, id=post_id)
    template_name = 'blog/detail.html'
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category, slug=slug, is_published=True)
    posts = get_all_posts().filter(category=category.id)
    context = {'post_list': posts, 'category': category}
    return render(request, template_name, context)
