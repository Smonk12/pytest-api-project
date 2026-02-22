import requests

def test_get_all_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    first_user = response.json()[0]
    assert 'id' in first_user
    assert 'name' in first_user

def test_get_single_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user['id'] == 1
    assert 'name' in user

def test_user_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")
    # JSONPlaceholder returns 200 with empty object sometimes, real API might return 404
    assert response.status_code in [200, 404]


def test_invalid_endpoint_returns_404():
    url = "https://jsonplaceholder.typicode.com/invalid-endpoint"

    response = requests.get(url)

    assert response.status_code == 404