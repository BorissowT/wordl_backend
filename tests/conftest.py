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

    # upload_test_data_to_mongo("apartment_configs",
    #                           f"{path}/test_datadump/mongo_dump"
    #                           f".apartment_configs.json")
    # upload_test_data_to_mongo("shared_configs",
    #                           f"{path}/test_datadump/mongo_dump"
    #                           f".shared_configs.json")
    # upload_test_data_to_mongo("clients",
    #                           f"{path}/test_datadump/mongo_dump.clients.json")

    # other setup can go here

    yield app

    # clean up / reset resources here

    # mongo.db["clients"].drop()
    # mongo.db["apartment_configs"].drop()
    # mongo.db["shared_configs"].drop()


@pytest.fixture(autouse=True)
def client(app):
    """Client to execute test requests like post, get etc.

    :param app: app instance
    :return: test client
    """
    return app.test_client()
