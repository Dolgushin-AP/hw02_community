from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group

# Главная страница
def index(request):    
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    # template = 'posts/index.html'
    # title = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# Страница сообществ
def group_posts(request, slug):
    template = 'posts/group_list.html'
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
    # template = 'posts/group_list.html'
    # title = 'Здесь будет информация о группах проекта Yatube'
    # context = {
    #    'title': title
    # }
    # return render(request, template, context)


# def posts_list(request, slug):
#     template = 'posts/group_list.html'
#     return render(request, template)