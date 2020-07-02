from django.db import models

from datetime import date
# Create your models here.
# В нем мы будем писать наши модели тоесть описывать таблицы в базе данных

# Импортируем models из django db
# Class Category наследуеться от класа Model


class Category(models.Model):
    # Категория
    # Тут мы описываем поля, они ще столбцы в таблице
    name = models.CharField('Категория', max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

# Возвращает строковое представление модели
    def __str__(self):
        return self.name

    class Meta:
        verbos_name = "Категория"
        verbos_name_plural = "Категории"


class Actor(models.Model):
    # Актеры и режисеры
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Изображения', upload_to="actors/")

    # Возвращает строковое представление модели

    def __str__(self):
        return self.name

    class Meta:
        verbos_name = "Категория"
        verbos_name_plural = "Категории"


class Genre(models.Model):
    # Жанры
    name = models.CharField('Категория', max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbos_name = "Категория"
        verbos_name_plural = "Категории"


class Movie(models.Model):
    # Фильмы
    title = models.CharField('Название', max_length=100)
    tagLine = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2019)
    country = models.CharField('Страна', max_length=30)
    directors = models.ManyToManyField(
        Actor, verbose_name='режисер', related_name="film_director")
    actors = models.ManyToManyField(
        Actor, verbos_name='Актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbos_name="Жанры")
    word_premiere = models.DateField('Примьера в мире', default=date.today)
    budget = models.PositiveSmallIntegerField(
        '', default=0, help_text='Указывать суммуу в долларах')
    fees_in_usa = models.PositiveSmallIntegerField(
        "Сборы в США", default=0, help_text='Указывать суммуу в долларах'
    )
    fees_in_world = models.PositiveSmallIntegerField(
        'Сборы в мире', default=0, help_text='Указывать суммуу в долларах'
    )
    category = models.ForeignKey(
        Category, verbos_name='', on_delete=models.SET_NULL, null=True)
