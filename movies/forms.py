#Тут мы будем писать формы
from django import forms
from django.forms import fields

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма для отзывов"""
    class Meta:
        model = Reviews
        fields = ("name","email","text")