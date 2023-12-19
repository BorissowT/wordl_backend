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


def test_if_new_player_cannot_join_with_wrong_game_id(client):
    """
    WHEN new player enters a game by invitation link with a wrong game ID
    THEN check if a '404' status code is returned
    """
    invitation_data = {"username": "tim_user", "skin": 9, "rounds": 2,
                       "lapTime": 2, "amountUsers": 2}

    response = client.post("/api/start/", json=invitation_data)
    response_json = response.json
    game_id = response_json.get('game_id')
    invited_user_data = {"username": "tim_user", "skin": 8}

    response = client.post(f"/api/start/{123}", json=invited_user_data)
    assert response.status_code == 404
    assert response.content_type == "application/json"


def test_if_game_id_is_the_same_when_new_player_joins_with_invitation_link(
        client):
    """
    WHEN new player enters a game by invitation link with a valid game ID
    THEN check if a '200' status code is returned
    and if game_id is same for both players
    """
    invitation_data = {"username": "tim_user", "skin": 9, "rounds": 2,
                       "lapTime": 2, "amountUsers": 2}

    response_of_start_player = client.post("/api/start/", json=invitation_data)
    response_json = response_of_start_player.json
    game_id_start_player = response_json.get('game_id')
    invited_user_data = {"username": "tim_user2", "skin": 8}
    response_of_new_player = client.post(f"/api/start/{game_id_start_player}",
                                         json=invited_user_data)

    assert response_of_new_player.status_code == 200
    assert response_of_new_player.content_type == "application/json"

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
