from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from ..common.exceptions import RecordAlreadyExists, RecordNotFound

from .models import Book


def create_book(book_data):
    book = Book(**book_data)
    try:
        book.save()

        # FIXME: this is DRY code, make it clean!
        # the problem may in db `flush()` method
        # because they not raise error even any
        # duplicate data value
        if not book.id:
            title = 'Book Already Exists'
            desc = f"Book {book_data.get('name')} already has been taken."
            raise RecordAlreadyExists(title, desc)

    except IntegrityError:
        title = 'IntegrityError'
        desc = f"Book {book_data.get('name')} may already taken."
        raise RecordAlreadyExists(title, desc)

    return book


def get_book_by_id(book_id):
    try:
        result = Book.query.filter(Book.id == book_id).one()
    except NoResultFound:
        title = 'Record Not Found'
        desc = f"There is no Book with `id: {book_id}`"
        raise RecordNotFound(title, desc)

    return result


def get_all_books():
    return Book.query.all()


def update_book(book_data, book_id):
    book = get_book_by_id(book_id)
    book.update(**book_data)

    return book


def delete_book(book_id):
    book = get_book_by_id(book_id)
    book.delete()
