import pytest


@pytest.fixture(autouse=True, scope='session')
def setup():
    print('pre condition')
    yield
    print('post condition')
