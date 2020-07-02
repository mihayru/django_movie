from django.db import models

from datetime import date
# Create your models here.
# В нем мы будем писать наши модели тоесть описывать таблицы в базе данных

# Импортируем models из django db
# Class Category наследуеться от класа Model

# Категория
# Тут мы описываем поля, они ще столбцы в таблице


class Category(models.Model):

    name = models.CharField('Категория', max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

# Возвращает строковое представление модели
    def __str__(self):
        return self.name

    class Meta:
        verbos_name = "Категория"
        verbos_name_plural = "Категории"

    # Актеры и режисеры


class Actor(models.Model):

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

    # Жанры


class Genre(models.Model):

    name = models.CharField('Категория', max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbos_name = "Категория"
        verbos_name_plural = "Категории"

    # Фильмы


class Movie(models.Model):

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


# Кадры из фильма
class MovieShots(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.CharField('Описание')
    image = models.ImageField('Изображения', upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадры из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):

    value = models.PositiveIntegerField('', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга '
        verbose_name_plural = 'Звезды рейтинга'

# Рейтинг


class Rating(models.Model):
    ip = models.CharField('', max_length=15)
    star = models.ForeignKey(
        RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(
        Movie, on_delete=models.CharField, verbose_name='фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг '
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self', verbos_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeingKey(
        Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв '
        verbose_name_plural = 'Отзывы'
