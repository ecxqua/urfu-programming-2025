# pages/urls.py
"""
URL-маршруты для приложения 'pages'.

Обрабатывает запросы к статическим (информационным) страницам сайта,
таким как «О проекте» и «Правила».

Используется пространство имён 'pages' для изоляции URL-имён
и предотвращения конфликтов с маршрутами других приложений.
"""

from django.urls import path
from . import views

# Пространство имён для корректной генерации URL (например, {% url 'pages:about' %})
app_name = 'pages'

urlpatterns = [
    # Страница «О проекте»
    path('about/', views.about, name='about'),
    
    # Страница «Правила»
    path('rules/', views.rules, name='rules'),
]