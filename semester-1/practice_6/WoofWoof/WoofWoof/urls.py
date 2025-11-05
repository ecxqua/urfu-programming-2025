"""WoofWoof URL Configuration
"""
from django.contrib import admin
# include позволяет подключать urls из приложения
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # все маршруты приложения dogs начинаются с /dogs/
    path('', include('dogs.urls')),
]
