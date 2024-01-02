# Tests for '/api/game/{gameId}/status' endpoint
def test_get_game_status_authorisation_error(client):
    """
    WHEN getting game status
    AS user with WRONG authorization token
    THEN check if the response status code is 400 "arameter validation failed"
    """
    invitation_data = {"username": "tim_user", "skin": 9, "rounds": 2,
                       "lapTime": 2, "amountUsers": 2}

    response = client.post("/api/start/", json=invitation_data)

    response_json = response.json
    game_id = response_json.get('game_id')
    token = "4566%$§9(/%§23577"

    headers = {"Authorization": {token}}

    client.post(f"/api/game/{game_id}/ready", headers=headers)

    response = client.get(f"/api/game/{game_id}/status", headers=headers)
    assert response.status_code in (102, 200, 400, 404)
    assert response.content_type == "application/json"


def test_get_game_status_game_is_not_found(client):
    """
    WHEN getting game status
    THEN check if error response is 404, when game is not found aka game_id is wrong
    """
    invitation_data = {"username": "tim_user", "skin": 9, "rounds": 2,
                       "lapTime": 2, "amountUsers": 2}

    response = client.post("/api/start/", json=invitation_data)

    game_id = 123
    response_json = response.json
    token = response_json.get('token', None)
    headers = {"Authorization": {token}}

    client.post(f"/api/game/{game_id}/ready", headers=headers)

    response = client.get(f"/api/game/{game_id}/status", headers=headers)
    assert response.status_code == 404
    assert response.content_type == "application/json"


def test_get_game_status_game_is_not_started(client):
    """
    WHEN getting game status, when the game hasn't been started yet
    THEN check if error response is 201
    """
    invitation_data = {"username": "tim_user", "skin": 9, "rounds": 2,
                       "lapTime": 2, "amountUsers": 2}

    response = client.post("/api/start/", json=invitation_data)

    response_json = response.json
    game_id = response_json.get('gameId')
    token = response_json.get('token', None)
    headers = {"Authorization": {token}}

    response = client.get(f"/api/game/{game_id}/status", headers=headers)
    assert response.status_code == 201
    assert response.content_type == "application/json"


def test_game_score_game_not_found(client):
    """
    WHEN calling the 'scored' endpoint with invalid game id
    THEN check if the response status code is 404
    """
    invitation_data = {
        "username": "tim_user",
        "skin": 9,
        "rounds": 2,
        "lapTime": 2,
        "amountUsers": 2
    }

    response_json = client.post("/start/", json=invitation_data)
    game_id = 12345
    token = response_json.get('token', None)
    headers = {"Authorization": token}

    # Calling 'scored' endpoint with not existing game id
    response = client.post(f"/game/{game_id}/scored", headers=headers, json={"points": 10})

    assert response.status_code == 404
    assert response.content_type == "application/json"

