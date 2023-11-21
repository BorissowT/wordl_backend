def test_200_code_as_user(client):
    """
    WHEN the /api/apartment-configs is called
    AS logged user
    THEN check that a '200' status code is returned
    """

    response = client.get("/api/start/",
                          headers={'Authorization': 'bearer '})

    assert response.status_code == 200
    assert response.content_type == "application/json"

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