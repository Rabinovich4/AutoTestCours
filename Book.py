class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f'Название книги {self.title}, Автор книги {self.author}, Кол-во страниц в книге {self.pages}')


book1 = Book("Война и мир", "Лев Толстой", 1225)
book2 = Book("Преступление и наказание", "Федор Достоевский", 331)

book1.display_info()
book2.display_info()