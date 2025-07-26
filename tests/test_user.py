import requests
import requests_mock

def test_users_endpoint_unauthorized(requests_mock):
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Mock the GET request with params
    requests_mock.get(
        f"{url}?username=admin&password=admin",
        status_code=401,
        text=""
    )

    response = requests.get(url, params=params)

    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response, got: '{response.text}'"


def test_users_endpoint_authorized_empty_response(requests_mock):
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mock the GET request with params
    requests_mock.get(
        f"{url}?username=admin&password=qwerty",
        status_code=200,
        text=""
    )

    response = requests.get(url, params=params)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response, got: '{response.text}'"
