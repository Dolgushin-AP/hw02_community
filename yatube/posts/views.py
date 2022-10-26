from django.shortcuts import get_object_or_404, render

from .models import Group, Post


POSTS_PER_PAGE = 10


def index(request):
    """ Возвращает главную страницу """
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    """ Сортировка постов по дате публикации """
    show_link = True
    """ Размещение информации в шаблон """
    context = {
        'posts': posts,
        'show_link': show_link,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """ Посты, отфильтрованные по группам """
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    """
    Возвращает сообщение об ошибке,
    если slug запроса не соответствует slug группы
    """
    posts = group.posts.all()[:POSTS_PER_PAGE]
    """ Метод .filter ограничивает поиск по критериям """
    show_link = True
    """ Словарь с данными """
    context = {
        'group': group,
        'posts': posts,
        'show_link': show_link,
    }
    return render(request, template, context)
