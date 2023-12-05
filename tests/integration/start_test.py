from unittest.mock import patch


def test_start_game_as_power_user_get_200code(client):
    """
    WHEN the /api/start is called
    AS anon user
    THEN check that a '200' status code is returned
    """
    response = client.post("/api/start",
                           data={"username": "tim_user", "skin": 8, "rounds": 2, "lapTime": 2, "amountUsers": 2})

    assert response.status_code == 200
    assert "gameId" in response.json()
    assert "token" in response.json()
    assert response.content_type == "application/json"


def test_enter_game_by_id(client):
    """
    WHEN entering a game by ID
    AS anon user
    THEN check if a '200' or '404' status code is returned based on the game ID existence
    """
    game_id = 123
    response = client.post("/api/start/{game_id}", data={"username": "tim_user", "skin": 8})

    assert response.status_code in (200, 404)


# Tests for '/api/game/{gameId}/status' endpoint
@patch('app.utils.resource_protector.ResourceProtector.acquire_token')
def test_get_game_status(client):
    """
    WHEN getting game status
    AS user with authorization token
    THEN check the response status code and content type
    """
    game_id = 123
    headers = {"Authorization": "Bearer YOUR_TOKEN"}
    response = client.get(f"/api/game/{game_id}/status", headers=headers)
    assert response.status_code in (102, 200, 400, 404)
    assert response.content_type == "application/json"


# Tests for '/api/game/{gameId}/ready' endpoint
def test_set_user_ready(client):
    """
    WHEN setting user status to 'ready'
    AS user with authorization token
    THEN check the response status code
    """
    game_id = 123
    headers = {"Authorization": "Bearer TOKEN"}
    response = client.post(f"/api/game/{game_id}/ready", headers=headers)
    assert response.status_code in (102, 200, 400, 403, 404)


# Tests for '/api/game/{gameId}/scored' endpoint
def test_user_solved_word(client):
    """
    WHEN a user solves a word
    AS user with authorization token
    THEN check the response status code and content type
    """
    game_id = 123
    headers = {"Authorization": "Bearer YOUR_TOKEN"}
    response = client.post(f"/api/game/{game_id}/scored", headers=headers)
    assert response.status_code in (102, 200, 400, 404)
    assert response.content_type == "application/json"


# Tests for '/api/start' endpoint
def test_start_game_invalid_payload(client):
    """
    WHEN the /api/start is called with invalid payload
    AS anon user
    THEN check that a '400' status code is returned
    """
    response = client.post("/api/start", json={"invalid_key": "invalid_value"})
    assert response.status_code == 400



# examples:
#
# @patch('app.utils.resource_protector.ResourceProtector.acquire_token')
# def test_get_objects_as_user(mocked_resource_protector, client):
#     """
#     WHEN the /api/apartment-configs is called
#     AS logged user "registered_user_sub_1"
#     THEN check if two objects of that user are returned
#     """
#
#     # prevent token validation and falsify token with test user
#     mocked_resource_protector.return_value = {'sub': 'registered_user_sub_1',
#                                               'preferred_username': 'username'}
#     response = client.get("/api/apartment-configs/",
#                           headers={'Authorization': 'bearer '})
#     data = response.json
#     assert response.status_code == 200
#     assert len(data) == 2
#     assert response.content_type == "application/json"
#
#
# @patch('app.utils.resource_protector.ResourceProtector.acquire_token')
# def test_get_null_objects(mocked_resource_protector, client):
#     """
#     WHEN the /api/apartment-configs is called
#     AS logged user "registered_user_sub_2"
#     THEN check if nothing is returned
#     """
#
#     # prevent token validation and falsify token with test user
#     mocked_resource_protector.return_value = {'sub': 'registered_user_sub_2',
#                                               'preferred_username': 'username'}
#     response = client.get("/api/apartment-configs/",
#                           headers={'Authorization': 'bearer '})
#     data = response.json
#     assert response.status_code == 200
#     assert len(data) == 0
#     assert response.content_type == "application/json"
#
#
# @patch('app.utils.resource_protector.ResourceProtector.acquire_token')
# def test_get_configs_by_apartments_id(mocked_resource_protector, client):
#     """
#     WHEN the /api/apartment-configs?apartment_id=id_for_test is called
#     AS logged user "registered_user_sub_3"
#     THEN check if 3 configs are returned
#     """
#
#     # prevent token validation and falsify token with test user
#     mocked_resource_protector.return_value = {'sub': 'registered_user_sub_3',
#                                               'preferred_username': 'username'}
#     response = client.get("/api/apartment-configs/?apartment_id=id_for_test",
#                           headers={'Authorization': 'bearer '})
#     data = response.json
#     assert response.status_code == 200
#     assert len(data) == 3
#     assert response.content_type == "application/json"
