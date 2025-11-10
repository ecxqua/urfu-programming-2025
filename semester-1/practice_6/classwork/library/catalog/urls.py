from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('books/', views.book_list_view, name='book_list'),
    path('books/<int:book_id>/', views.book_detail_view, name='book_detail'),
]
