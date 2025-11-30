# blog/urls.py
"""
URL-маршруты для приложения 'blog'.

Определяет маршруты, связанные с отображением:
- Главной страницы блога
- Детальной страницы поста
- Страницы постов по категории

Используется пространство имён (namespace) 'blog' для изоляции URL-имён
от других приложений в проекте.
"""

from django.urls import path
from . import views

# Пространство имён для URL-имён (например, blog:index)
app_name = 'blog'

urlpatterns = [
    # Главная страница блога — список всех постов
    path('', views.index, name='index'),
    
    # Детальная страница поста по числовому ID
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    
    # Список постов по категории (категория передаётся как slug)
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]