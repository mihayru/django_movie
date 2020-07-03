from django.contrib import admin
from .models import Category,Genre,Movie,MovieShots,Actor,RatingStar,Rating,Reviews


# Register your models here.
#Описываем модели которые хотим зарегистрировать и выводить в административной панели DJANGO
#Тут можем написать логику для изминения поведения админки

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)

