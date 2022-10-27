from django.shortcuts import get_object_or_404, render

from .models import Group, Post


POSTS_PER_PAGE = 10


def index(request):
    """ Возвращает главную страницу """
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """ Посты, отфильтрованные по группам """
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
