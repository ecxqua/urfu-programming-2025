from datetime import datetime


class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        title (str): Название книги
        author (str): Автор книги
        year (str): Год публикации в формате строки
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
        return self.info()

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title

    def info(self):
        """
        Возвращает строку с основной информацией о книге.

        Returns:
            Строка в формате: "Название Автор Год"
        """
        return f"{self.title} {self.author} {self.year}"

    @property
    def age(self):
        return datetime.now().year - self.year

    @age.setter
    def age(self, value):
        self.year = datetime.now().year - value

    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(';')
        return cls(title, author, int(year))


book1 = Book('Название книги', 'Автор А. А.', 2019)
print(book1.info())
print(book1)
book3 = Book('Море', 'Василий', 2021)
print('book1 == book3:', book1 == book3)
print(str(book3))

print('Возраст книги 1:', book1.age, 'лет')
book1.age = 25
print('Возраст книги 1:', book1.age, 'лет')

book4 = Book.from_string('Лето;Анна;1984')
print(str(book4))

# class Ebook(Book):
#     def __init__(self, title: str, author: str, year: int, format: str):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.format = format

#     def info(self):
#         return f"{self.title} {self.author} {self.year} {self.format}"


# book2 = Ebook('Название книги', 'Автор А. А.', 2025, 'Электронная')
# print(book2.info())
