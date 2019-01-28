import pytest
from _pytest.runner import runtestprotocol

from falcon import testing

from core.routes import get_app
from core.api.common.database import db_session, init_db, drop_db

HEADERS = {
    'content-type': 'application/json'
}


@pytest.fixture(scope='session')
def app(request):
    """
    Create new application.
    Establish a context so all application parts
    are properly functioning.
    """
    app = get_app()

    def teardown():
        pass

    request.addfinalizer(teardown)

    return app


@pytest.fixture(scope='session')
def test_client(app, request):
    """
    Init falcon test client.
    """
    client = testing.TestClient(app)

    return client


@pytest.fixture(scope='function')
def session(app):
    session = db_session
    session.begin_nested()

    yield session

    session.rollback()


@pytest.fixture(scope='session')
def custom_headers():
    return HEADERS


@pytest.fixture(scope="session", autouse=True)
def database_management(request):
    """
    Create database before running the first test.
    Drop the database after running the last test.
    """
    init_db()

    def teardown():
        db_session.close()
        db_session.remove()
        drop_db()

    request.addfinalizer(teardown)


def pytest_runtest_protocol(item, nextitem):
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            print('\n\t%s --- %s' % (item.name, report.outcome))
    return True
