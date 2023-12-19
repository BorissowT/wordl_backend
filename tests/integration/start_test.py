from unittest.mock import patch

import pytest


def test_start_game_as_power_user_get_200code(client):
    """
    WHEN the /api/start is called
    THEN check that a '200' status code is returned
    """
    response = client.post("/api/start",
                           data={"username": "tim_user", "skin": 8, "rounds": 2, "lapTime": 2, "amountUsers": 2})
    assert response.status_code == 200
    assert "gameId" in response.json()
    assert "token" in response.json()
    assert response.content_type == "application/json"


def test_start_game_invalid_skin(client):
    """
    WHEN the /api/start is called with an invalid skin value
    THEN check that a '400' status code is returned
    """
    invalid_skin_value = 11  # value above the acceptable range (1-10)
    response = client.post("/api/start",
                           json={"username": "tim_user", "skin": invalid_skin_value, "rounds": 2, "lapTime": 2,
                                 "amountUsers": 2})
    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_start_game_invalid_rounds(client):
    """
    WHEN the /api/start is called with an invalid rounds value
    THEN check that a '400' status code is returned
    """
    round_value = 6  # rounds above the acceptable range (1-5)
    response = client.post("/api/start",
                           json={"username": "tim_user", "skin": 9, "rounds": round_value, "lapTime": 2,
                                 "amountUsers": 2})
    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_start_game_invalid_lapTime(client):
    """
    WHEN the /api/start is called with an invalid lapTime value
    THEN check that a '400' status code is returned
    """
    lap_time_value = 80  # lapTime above the acceptable range (1-60)
    response = client.post("/api/start",
                           json={"username": "tim_user", "skin": 9, "rounds": 4, "lapTime": lap_time_value,
                                 "amountUsers": 2})
    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_start_game_invalid_ammount_of_users(client):
    """
    WHEN the /api/start is called with an invalid amount of users value
    THEN check that a '400' status code is returned
    """
    amount_of_users_value = 80  # lapTime above the acceptable range (1-10)
    response = client.post("/api/start",
                           json={"username": "tim_user", "skin": 9, "rounds": 4, "lapTime": 5,
                                 "amountUsers": amount_of_users_value})
    assert response.status_code == 400
    assert response.content_type == "application/json"


@pytest.mark.parametrize("invalid_field, value",
                         [("amountUsers", "invalid"), ("lapTime", "invalid"), ("rounds", "invalid"),
                          ("skin", "invalid")])
def test_start_game_invalid_integer_fields(client, invalid_field, value):
    """
    WHEN the /api/start is called with a string value instead of an integer in the request body for a specific field
    THEN check that a '400' status code is returned for the invalid integer field
    """
    request_body = {"username": "tim_user", "skin": 5, "rounds": 2, "lapTime": 2, "amountUsers": 2,
                    invalid_field: value}
    response = client.post("/api/start", json=request_body)
    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_start_game_empty_username(client):
    """
    WHEN the /api/start is called with an empty username
    THEN check that a '400' status code is returned
    """
    response = client.post("/api/start", json={"username": "", "skin": 5, "rounds": 2, "lapTime": 2, "amountUsers": 2})
    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_start_game_missing_username(client):
    """
    WHEN the /api/start is called with missing username
    THEN check that a '400' status code is returned
    """
    request_body = {
        "skin": 5,
        "rounds": 2,
        "lapTime": 2,
        "amountUsers": 2
    }
    response = client.post("/api/start", json=request_body)
    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_start_game_missing_skin(client):
    """
    WHEN the /api/start is called with missing skin
    THEN check that a '400' status code is returned
    """
    request_body = {
        "username": "tim_user",
        "rounds": 2,
        "lapTime": 2,
        "amountUsers": 2
    }
    response = client.post("/api/start", json=request_body)
    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_start_game_missing_rounds(client):
    """
    WHEN the /api/start is called with missing rounds
    THEN check that a '400' status code is returned
    """
    request_body = {
        "username": "tim_user",
        "skin": 5,
        "lapTime": 2,
        "amountUsers": 2
    }
    response = client.post("/api/start", json=request_body)
    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_start_game_missing_lapTime(client):
    """
    WHEN the /api/start is called with missing lapTime
    THEN check that a '400' status code is returned
    """
    request_body = {
        "username": "tim_user",
        "skin": 5,
        "rounds": 2,
        "amountUsers": 2
    }
    response = client.post("/api/start", json=request_body)
    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_start_game_missing_amountUsers(client):
    """
    WHEN the /api/start is called with missing amountUsers
    THEN check that a '400' status code is returned
    """
    request_body = {
        "username": "tim_user",
        "skin": 5,
        "rounds": 2,
        "lapTime": 2
    }
    response = client.post("/api/start", json=request_body)

    assert response.status_code == 400
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
