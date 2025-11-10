from django.shortcuts import render


def book_list_view(request):
    books = [
        {'id': 1, 'title': 'Книга 1'},
        {'id': 2, 'title': 'Книга 2'},
        {'id': 3, 'title': 'Книга 3'},
    ]
    return render(request, 'catalog/book_list.html', {'books': books})


def book_detail_view(request, book_id):
    book = {
        'id': book_id,
        'title': f'Пример книги {book_id}',
        'author': 'Автор книги',
        'year': 2024,
        'isbn': '1234567890',
        'description': 'Описание книги...',
        'copies_available': 5
    }
    return render(request, 'catalog/book_detail.html', {'book': book})
