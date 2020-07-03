# Для указание какие URL будут в нашем приложении(Создаем сами )

from django.urls import path

from . import views

urlpatterns = [
    path('', views.MoviesView.as_view())

]
