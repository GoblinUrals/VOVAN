class Library:
    def __init__(self):
        self.available_book = {}

    def add_book(self, book_name, book_rating):
        if book_name not in self.available_book.keys():
            book = {}
            book[book_name] = book_rating
            self.available_book[book_name] = book
        else:
            print(f"{book_name} Книга уже есть в библиотеке {self.available_book.get(book_name)}")

    def change_book_rating(self, book_name, new_rating):
        if book_name not in self.available_book.keys():
            print(f"\n{book_name} Книги нет в библиотеке")
        else:
            book = self.available_book.get(book_name)
            book[book_name] = new_rating
            print(f"\n{book_name} Книга получила новый рейтинг{new_rating}")

    def get_all_books(self):
        print(f"\n{self.available_book}")


    def delete_book(self, book_name):
        if book_name not in self.available_book.keys():
            print(f"\n{book_name} Книги нет в библиотеке")
        else:
            self.available_book.pop(book_name)
            print(f"\n{book_name} Книга удалена из библиотеки")

    def get_book_by_name(self, book_name):
        if book_name not in self.available_book.keys():
            print(f"\n{book_name} Книги не существует в библиотеки")
        else:
            book = self.available_book.get(book_name)
            print('\nЗдесь', book)

    def get_book_by_ratings(self, book_ratings):
        books = self.available_book.values()
        book_same_rating = {}
        for book in books:
            if book_ratings in book.values():
                book_same_rating.update(book)
        print('\nКнига без рейтинга %s' %(book_ratings) if book_same_rating == {} else print(book_same_rating) )

library = Library()

library.add_book(book_name = 'Стрелок',book_rating = 7 )
library.add_book(book_name = 'Стрелок',book_rating = 7 )
library.add_book(book_name = 'Мидуэй',book_rating = 7.58 )
library.add_book(book_name = 'Снайпер',book_rating = 8.5 )
library.add_book(book_name = 'Джон Уик',book_rating = 9.5 )
library.get_all_books()
library.add_book(book_name = 'Мэверик',book_rating = 9.5 )
library.change_book_rating(book_name = 'Стелла',new_rating = 8 )
library.change_book_rating(book_name = 'Стрелок',new_rating = 8 )
library.get_all_books()
library.delete_book(book_name = 'Старуха')
library.delete_book(book_name = 'Стелла')
library.get_book_by_name(book_name = 'Стелла')
library.get_book_by_name(book_name = 'Стрелок')
library.get_all_books()