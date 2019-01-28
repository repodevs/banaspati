import pytest

from sqlalchemy.exc import IntegrityError

from ..models import Book


def test_create_book_implicitly():
    payload = {
        'name': 'Foo Book',
        'author': 'Bar Author',
        'isbn': 1234121
    }

    book = Book(**payload)
    book.save()

    assert book.name == payload['name']


def test_create_book_wrong_params():
    payload = {
        'xname': 'Foo Book',
        'xauthor': 'Bar Author',
        'isbn': 1234121
    }

    book = Book(**payload)
    book.save()

    assert not book.name


def test_create_book_with_session(session):
    payload = {
        'name': 'Foo Book Session',
        'author': 'Bar Author',
        'isbn': 1234121
    }

    book = Book(**payload)
    session.add(book)
    session.flush()

    assert book.name == payload['name']


def test_create_book_name_is_unique(session):
    payload = {
        'name': 'Foo Book Unique',
        'author': 'Bar Author',
        'isbn': 1234121
    }

    book = Book(**payload)
    session.add(book)
    session.flush()

    with pytest.raises(IntegrityError):
        book2 = Book(**payload)
        session.add(book2)
        session.flush()
