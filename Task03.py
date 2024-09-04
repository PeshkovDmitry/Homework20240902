
class Book:

    current_counter = 1

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._id_counter = Book.current_counter
        Book.current_counter += 1
        return obj

    def __str__(self):
        return f"Книга №{self._id_counter}"


book_1 = Book()
book_2 = Book()
book_3 = Book()
print(book_1, book_2, book_3)