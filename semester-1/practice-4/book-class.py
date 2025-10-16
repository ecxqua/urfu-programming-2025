class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        title (str): Название книги
        author (str): Автор книги
        year (str): Год публикации в формате строки
    """

    def __init__(self, title: str, author: str, year: str):
        """
        Инициализирует экземпляр книги.

        Args:
            title: Название книги
            author: Автор книги
            year: Год публикации (в формате строки)
        """
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        """
        Возвращает строку с основной информацией о книге.

        Returns:
            Строка в формате: "Название Автор Год"
        """
        return f"{self.title} {self.author} {self.year}"


book1 = Book('Название книги', 'Автор А. А.', '10-12-2025')
print(book1.info())
