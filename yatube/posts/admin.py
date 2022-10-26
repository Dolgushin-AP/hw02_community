from django.contrib import admin

from .models import Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Создание админки с полями """
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    """ Редактирование group в любом посте из списка постов """
    list_editable = ('group',)
    """ Поиск по тексту постов """
    search_fields = ('text',)
    """ Фильтрация по дате """
    list_filter = ('pub_date',)
    """ Для пустых колонок будет эта строка """
    empty_value_display = '-пусто-'


@admin.register(Group)
class Group(admin.ModelAdmin):
    """ Создание админки с полями """
    list_display = ('pk', 'title', 'slug', 'description')
    """ Для пустых колонок будет эта строка """
    empty_value_display = '-пусто-'
