# pages/views.py
"""
Статические страницы сайта.

Содержит представления для страниц «О проекте» и «Правила»,
которые не зависят от динамических данных и отображают
фиксированное содержимое.
"""

from django.shortcuts import render


def about(request):
    """Отображает страницу «О проекте».

    Эта страница содержит информацию о целях и истории создания проекта.
    """
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Отображает страницу «Правила».

    Содержит правила использования сайта, поведения пользователей
    и другие нормативные положения.
    """
    template = 'pages/rules.html'
    return render(request, template)