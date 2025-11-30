"""blogicum URL Configuration

Корневой URLconf проекта. Определяет основные маршруты и подключает
URL-конфигурации отдельных приложений (blog, pages и т.д.).

Основные принципы:
- Используется `include()` для подключения URL-пространств каждого приложения.
- Каждое приложение зарегистрировано с указанием **instance namespace**
  (например, `namespace='blog'`), что позволяет безопасно использовать
  именованные URL в шаблонах через `{% url 'blog:index' %}`.
- Административный интерфейс подключён по стандартному пути `/admin/`.

Ссылка на документацию:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Административная панель Django
    path('admin/', admin.site.urls),

    # Основное приложение блога — подключено с пространством имён 'blog'
    path('', include('blog.urls', namespace='blog')),

    # Статические страницы («О проекте», «Правила» и т.п.) — пространство имён 'pages'
    path('pages/', include('pages.urls', namespace='pages')),
]