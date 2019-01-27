import json
import falcon

from .domain import create_book, get_book_by_id, get_all_books, delete_book, update_book


class BookResource(object):

    def on_get(self, req, resp, book_id):
        book = get_book_by_id(book_id)
        resp.body = json.dumps(book)
        resp.status = falcon.HTTP_200

    def on_get_all_books(self, req, resp):
        books = get_all_books()
        resp.body = json.dumps(books)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        book_data = req.media
        book_obj = create_book(book_data)
        resp.body = json.dumps(book_obj)
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp, book_id):
        book_data = req.media
        book_obj = update_book(book_data, book_id)
        resp.body = json.dumps(book_obj)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, book_id):
        delete_book(book_id)
        resp.status = falcon.HTTP_204  # https://stackoverflow.com/a/2342589
