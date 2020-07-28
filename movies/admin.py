from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, RatingStar, Rating, Reviews


# Register your models here.
# Описываем модели которые хотим зарегистрировать и выводить в административной панели DJANGO
# Тут можем написать логику для изминения поведения админки
# В данном файле мы будем писать класы с помощью которых будет конфигурировать нашу административную панель

# Отображение в категории


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)

#Для того чтобы мы видели все записи которые прикрепленны к данному фильму - Отображаеться в админке к каждому отдельному фильму
class ReviewInLine(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ('name','email')
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ('title',"category__name",)
    inlines = [ReviewInLine]
    #Кнопки сохранения вверху
    save_on_top = True
    #Сохраняем новый екземпляр из старго фильма
    save_as = True
    #Для того чтобы менять из списка в черновик
    list_editable = ("draft",)
    #Групировка полей
    fieldsets = (
        (None,{
           "fields":(("title","tagline"),)
           }),
        (None,{
           "fields":(("description","poster"),)
           }),
        (None,{
           "fields":(("year","world_premiere","country"),)
           }),
        ("Actors",{
            #Делаем чтобы эта группа находилась в свернутом виде
            "classes":("collapse",),
           "fields":(("actors","directors","genres","category"),)
           }),
        (None,{
           "fields":(("budget","fess_in_world","fees_in_usa"),)
           }),
        ("Options",{
           "fields":(("url","draft"),)
           }),
    )
@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
        """Жанры"""
        list_display = ("name","url")

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
        """Кадры из фильма"""
        list_display = ("title","movie")
        
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
        """Рейтинг"""
        list_display = ("name","ip")

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
        """Рейтинг"""
        list_display = ("name","age")


admin.site.register(RatingStar)

