import json


def test_create_book(test_client, custom_headers):
    payload = {
        'name': 'Foo Book',
        'author': 'Bar Author',
        'isbn': 1234321
    }
    r = test_client.simulate_post('/book',
                                  body=json.dumps(payload),
                                  headers=custom_headers)

    assert r.status_code == 200


def test_create_book_wrong_params(test_client, custom_headers):
    payload = {
        'xname': 'Foo Book',
        'xauthor': 'Bar Author',
        'isbn': 1234321
    }
    r = test_client.simulate_post('/book',
                                  body=json.dumps(payload),
                                  headers=custom_headers)

    assert r.status_code == 400


def test_get_book_detail(test_client, custom_headers):
    payload = {
        'name': 'Foo Book Detail',
        'author': 'Bar Author',
        'isbn': 1234321
    }
    res = test_client.simulate_post('/book',
                                    body=json.dumps(payload),
                                    headers=custom_headers)
    book_id = int(res.headers.get('book-id', 0))
    book_detail = {'id': book_id,
                   'name': 'Foo Book Detail',
                   'author': 'Bar Author',
                   'isbn': 1234321
                   }

    assert book_detail == res.json
