import os

import pytest as pytest

from app.run import create_app


@pytest.fixture(autouse=True)
def app():
    """
    Create test application instance. Upload test data.

    :return: configured app instance
    """

    app = create_app()
    path = os.path.dirname(os.path.abspath(__file__))


    yield app

    # clean up / reset resources here



@pytest.fixture(autouse=True)
def client(app):
    """Client to execute test requests like post, get etc.

    :param app: app instance
    :return: test client
    """
    return app.test_client()
