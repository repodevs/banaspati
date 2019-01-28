import falcon
from falcon import API

from core.api.common.middleware import (
    AfterRequestMiddleware,
    ContextMiddleware,
    RequireJSON
)
from core.api.book.resource import BookResource


def get_app() -> API:
    """ Init Book App
    """

    book_resource = BookResource()

    _app = falcon.API(middleware=[
        AfterRequestMiddleware(),
        ContextMiddleware(),
        RequireJSON()
    ])

    # Book Resource
    _app.add_route('/book', book_resource)
    _app.add_route('/book/{book_id:int}', book_resource)
    _app.add_route('/books', book_resource, suffix='all_books')

    return _app
