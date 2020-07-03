from django.shortcuts import render

# Create your views here.
# Логика нашего приложения
# В этом файле мы пишем функции и классы которые принимаю веб-запросы и возвращают ответ
# Этими ответами может быть html или направление или ошибка 404
from django.views.generic.base import View

from .models import Movie


class MoviesView(View):
    # Список фильмов
    # Создаем метод get который будед принимать GET запросы HTTP
    # Он принимает request - это вся информация присланная от нашего клиента(от браузера)
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {"movie_list": movies})


class MovieDetailView(View):
    # Полное описание фильма
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movies/movie_detail.html", {"movie": movie})
