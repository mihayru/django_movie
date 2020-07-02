"""
ASGI config for django_movie project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
#Нужен для асинхронных веб-серверов и приложений,являеться духовным наследником wsgi предназначеным
#для обеспичения синхронного взаимодействия между синхронными веб серверами платформами и преложениями python
#предостваляет стандарт как для асинхронных так и для синхронных реализации обратной совместимости wsgi
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_movie.settings')

application = get_asgi_application()
