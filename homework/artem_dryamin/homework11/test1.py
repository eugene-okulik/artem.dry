class Book:
    material = 'бумага'
    text = True

    def __init__(self, title, author, count_str, isbn, rezerv=False):
        self.title = title
        self.author = author
        self.count_str = count_str
        self.isbn = isbn
        self.rezerv = rezerv


book1 = Book('Идиот', 'Достоевский', 500, 12345)
book2 = Book('На дне', 'Горький', 160, 543)
book3 = Book('Старуха Изергиль', 'Горький', 125, 544)
book4 = Book('Собачье сердце', 'Булгаков', 350, 786)
book5 = Book('Мастер и Маргарита', 'Булгаков', 500, 787)
book4.rezerv = True


def new_form(book):
    new_text = f'Название: {book.title}, Автор: {book.author}, страниц: {book.count_str}, материал: {book.material}'
    if book.rezerv:
        print(f'{new_text}, зарезервирована')
    else:
        print(new_text)


new_form(book1)
new_form(book2)
new_form(book3)
new_form(book4)
new_form(book5)


class SchoolBook(Book):

    def __init__(self, title, author, count_str, isbn, prdmt, grup, zadaniya=True, rezerv=False):
        super().__init__(title, author, count_str, isbn, rezerv)
        self.prdmt = prdmt
        self.grup = grup
        self.zadaniya = zadaniya


new_book1 = SchoolBook('Алгебра', 'Антонов', 250, 6543, 'Алгебра', 9)
new_book2 = SchoolBook('Геометрия', 'Литвинов', 220, 6544, 'Геометрия', 10)
new_book2.rezerv = True


def new_func(new_book):
    new_text2 = (
        f'Название: {new_book.title}, Автор: {new_book.author}, '
        f'страниц: {new_book.count_str}, предмет: {new_book.prdmt}, класс: {new_book.grup}')
    if new_book.rezerv:
        print(f'{new_text2}, зарезервирована')
    else:
        print(new_text2)


new_func(new_book1)
new_func(new_book2)
