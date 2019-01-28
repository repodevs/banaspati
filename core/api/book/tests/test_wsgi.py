from falcon import API

from core.wsgi import app


def test_wsgi():
    assert isinstance(app, API)
