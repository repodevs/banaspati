from . import backend


def create_book(book_data):
    """Create Book.

    :param book_data: Book information
    :type book_data: dict
    :return: serialized Book object
    :type: dict
    """
    book = backend.create_book(book_data)

    return book.to_dict()


def get_book_by_id(book_id):
    """Get Book by id

    :param book_id: id of the book to be retrived
    :type book_id: integer
    :return: serialized Book object
    :rtype: dict
    """
    book = backend.get_book_by_id(book_id)

    return book.to_dict()


def get_all_books():
    """Get all Books.

    :return: serialized Book object
    :rtype: list
    """
    books = backend.get_all_books()

    return [
        book.to_dict() for book in books
    ]


def update_book(book_data, book_id):
    """Update Book.

    :param book_data: Book information
    :param book_id: id of the Book to be updated
    :return: serialized Book object
    :rtype: dict
    """
    book = backend.update_book(book_data, book_id)

    return book.to_dict()


def delete_book(book_id):
    """Delete Book.

    :param book_id: id of the Book to be deleted
    :type book_id: integer
    """
    backend.delete_book(book_id)
