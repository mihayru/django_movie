from django.shortcuts import render, redirect

# Create your views here.
# Логика нашего приложения
# В этом файле мы пишем функции и классы которые принимаю веб-запросы и возвращают ответ
# Этими ответами может быть html или направление или ошибка 404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm

from .models import Movie, Category


class MoviesView(ListView):
    # Список фильмов
    # Создаем метод get который будед принимать GET запросы HTTP
    # Он принимает request - это вся информация присланная от нашего клиента(от браузера)
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name =  'movies/movie_list.html'

    """Добавляем Категории фильмов"""

    def get_context_data(self, *args, **kwargs):
        # вызываем метод супер нашего родителя таким образом мы получаем словарь и заносим его в context
        context = super().get_context_data(*args, **kwargs)
        # Добавляем ключ categories и заносим query set всех нашых категорий
        context["categories"] = Category.objects.all()
        return context


class MovieDetailView(DetailView):
    # Полное описание фильмаA  
    model = Movie
    slug_field = "url"
    """Добавляем Категории фильмов"""

    def get_context_data(self, *args, **kwargs):
        # вызываем метод супер нашего родителя таким образом мы получаем словарь и заносим его в context
        context = super().get_context_data(*args, **kwargs)
        # Добавляем ключ categories и заносим query set всех нашых категорий
        context["categories"] = Category.objects.all()
        return context


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            # Говорим о том что хотим приостановить сохранение нашей формы
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie_id = movie
            form.save()
        return redirect(movie.get_absolute_url())
