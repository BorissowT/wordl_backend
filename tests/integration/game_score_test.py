def test_game_score_game_not_found(client):
    """
    WHEN calling the 'scored' endpoint with invalid game id
    THEN check if the response status code is 404
    """
    invitation_data = {"username": "tim_user",
                       "skin": 9,
                       "rounds": 2,
                       "lapTime": 2,
                       "amountUsers": 2}

    response = client.post("/api/start/", json=invitation_data)
    response_json = response.json
    game_id = 12345 #invalid game_id
    token = response_json.get('token', None)
    headers = {"Authorization": token}

    client.post(f"/api/game/{game_id}/ready", headers=headers)

    # Calling 'scored' endpoint with not existing game id
    response = client.post(f"/api/game/{game_id}/scored", headers=headers, json={"points": 10})

    assert response.status_code == 404
    assert response.content_type == "application/json"