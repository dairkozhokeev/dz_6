

class Book:
    if __name__ == '__main__':

        def __init__(self, title, author, year, read):
            self.title = title
            self.author = author
            self.year = year
            self.read = read
            self.read = 'непрочитана'

        def mark_as_read(self):
            self.read = 'прочитана'
            return self.read

        def mark_as_unread(self):
            self.read = 'непрочитана'
            return self.read

        def __str__(self):
            return  f'Book:{self.title}, author:{self.author}, year:{self.year}, read:{self.read}'

class Library(Book):
    def list_of_books(self, list_of_books):
        self.list_of_books = list_of_books

    def add_book(self,book):
        self.list_of_books.append(book)

    def list_books(self):
        return self.list_of_books

    def find_by_title(self, title):
        if title in self.list_of_books():
            return f'title:{title}, author:{self.author}, year:{self.year}, read:{self.read}'
        else:
            print('Книга не найдена!')

    def find_by_author(self, author):
        if author in self.list_of_books():
            return f'title:{self.title}, author:{self.author}, year:{self.year}, read:{self.read}'
        else:
            print('Книга не найдена!')

    def mark_book_as_read(self,title):
        if title in self.list_of_books():
            self.read = 'прочитана'
        else:
            print('книга не найдена!')

    def remove_book(self, title):
        for book in self.list_of_books():
            if book.title == title:
                self.list_of_books().remove(book)
                return f"книга {title} удалена"

    def sorted_books(self):   #???
        sorted_books = sorted(self.list_of_books(key = lambda x: x.read))
        return sorted_books

    def sorted_books_by_year(self):
        sorted_books_by_year = sorted(self.list_of_books(key = lambda x: x.year))
        return sorted_books_by_year


# while 1:
#     choose = input('Введите:\n1 если хотите добавить книгу в библиотеку\n2 если хотите вывевести лист книг в библиотеке'
#                    '\n3 если хотите найти книгу по названию'
#                    '\n4 если хотите найти книгу по ее автору\n5 если хотите отметить статус книги')
#     if choose == 'стоп':
#         break
#     elif choose == 1:
#         book_input = input('Введите название книги')
#         (Library.add_book(book_input))
#     elif choose == 2:
#         print(list_of_books)


