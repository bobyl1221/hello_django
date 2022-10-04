"""
Конфигурация ASGI для проекта hello_django.

Он предоставляет вызываемый ASGI как переменную уровня модуля с именем «приложение».

Дополнительные сведения об этом файле см.
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

application = get_asgi_application()
