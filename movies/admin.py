from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews

from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.
# Описываем модели которые хотим зарегистрировать и выводить в административной панели DJANGO
# Тут можем написать логику для изминения поведения админки
# В данном файле мы будем писать класы с помощью которых будет конфигурировать нашу административную панель


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


# Для того чтобы мы видели все записи которые прикрепленны к данному фильму - Отображаеться в админке к каждому отдельному фильму


class ReviewInLine(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


# Делаем чтобы в админке фильмов отображались кадры фильмов
class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    # Должно быть кортежем или списком поэтому в конец добавляем кому
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="90"')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ('title', "category__name",)
    inlines = [ReviewInLine, MovieShotsInline]
    readonly_fields = ("get_image",)
    # Кнопки сохранения вверху
    save_on_top = True
    # Сохраняем новый екземпляр из старго фильма
    save_as = True
    # Для того чтобы менять из списка в черновик
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    form = MovieAdminForm
    # Групировка полей
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", "poster", "get_image")
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            # Делаем чтобы эта группа находилась в свернутом виде
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fess_in_world", "fees_in_usa"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )

    # Должно быть кортежем или списком поэтому в конец добавляем кому

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Постер"

    # Пишем свои action для админки
    """Actions"""
    def unpublish(self, request, queryset):
        """Снять с публикации """
        # Обновляем наше поле драфт
        row_update = queryset.update(draft=True)
        # проверяем мы обновили одну запись или несколько в зависимости от этого выстраиваем нужное нам сообщеие
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей было обновлено'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей было обновлено'
        self.message_user(request, f'{message_bit}')

    publish.short_description = "Опубликовать"
    # чтобы применять данный екшн у пользователя должны быть права
    publish.allowed_permissions = ('change',)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    # Выводим кадры из фильма в админке.

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("movie", "ip")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    # Выводим фото актерев из фильма в админке.

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


admin.site.register(RatingStar)

admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"
