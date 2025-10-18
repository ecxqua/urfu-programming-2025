from datetime import datetime
from abc import ABC, abstractmethod


class Printable(ABC):
    """Абстрактный базовый класс для объектов, поддерживающих печать информации."""

    @abstractmethod
    def print_info(self):
        """Абстрактный метод для вывода информации об объекте."""
        pass


class Book(Printable):
    """
    Класс, представляющий книгу.

    Атрибуты:
        title (str): Название книги
        author (str): Автор книги
        year (int): Год публикации
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Инициализирует экземпляр книги.

        Args:
            title: Название книги
            author: Автор книги
            year: Год публикации 
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Возвращает строковое представление книги."""
        return self.info()

    def __eq__(self, other):
        """Сравнивает книги по названию."""
        return isinstance(other, Book) and self.title == other.title

    def info(self):
        """
        Возвращает строку с основной информацией о книге.

        Returns:
            Строка в формате: "Название Автор Год"
        """
        return f"{self.title} {self.author} {self.year}"

    def print_info(self):
        """Реализация абстрактного метода - возвращает информацию о книге."""
        return self.info()

    @property
    def age(self):
        """Возвращает возраст книги в годах."""
        return datetime.now().year - self.year

    @age.setter
    def age(self, value):
        """Устанавливает год публикации на основе желаемого возраста книги."""
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, data):
        """
        Создает объект книги из строки.

        Args:
            data: Строка с данными в формате "Название;Автор;Год"

        Returns:
            Новый экземпляр класса Book
        """
        title, author, year = data.split(';')
        return cls(title, author, int(year))


# Демонстрация работы класса Book
print("=== Демонстрация класса Book ===")

# Создание и тестирование book1
book1 = Book('Название книги', 'Автор А. А.', 2019)
print('book1.print_info():', book1.print_info())
print('book1.info():', book1.info())
print('book1:', book1)

# Создание и сравнение книг
book3 = Book('Море', 'Василий', 2021)
print('book1 == book3:', book1 == book3)
print('str(book3):', str(book3))

# Работа со свойством age
print('Возраст книги 1:', book1.age, 'лет')
book1.age = 25
print('После установки возраста 25 лет:')
print('Возраст книги 1:', book1.age, 'лет')
print('Год публикации книги 1:', book1.year)

# Создание книги из строки
book4 = Book.from_string('Лето;Анна;1984')
print('str(book4):', str(book4))


class Ebook(Book):
    """
    Класс, представляющий электронную книгу.

    Наследует от класса Book и добавляет информацию о формате.

    Атрибуты:
        title (str): Название книги
        author (str): Автор книги  
        year (int): Год публикации
        format (str): Формат электронной книги (например, PDF, EPUB)
    """

    def __init__(self, title: str, author: str, year: int, format: str):
        """
        Инициализирует экземпляр электронной книги.

        Args:
            title: Название книги
            author: Автор книги
            year: Год публикации
            format: Формат электронной книги
        """
        # Вызов конструктора родительского класса
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        """
        Возвращает строку с информацией об электронной книге.

        Returns:
            Строка в формате: "Название Автор Год Формат"
        """
        return f"{self.title} {self.author} {self.year} {self.format}"


# Демонстрация работы класса Ebook
print("\n=== Демонстрация класса Ebook ===")
book2 = Ebook('Название книги', 'Автор А. А.', 2025, 'Электронная')
print(book2.info())

# Демонстрация полиморфизма
print("\n=== Демонстрация полиморфизма ===")
books = [book1, book2, book3, book4]
for book in books:
    print(f"Тип: {type(book).__name__}, Информация: {book.print_info()}")
