import requests
import pytest

BASE = "http://127.0.0.1:5000"


@pytest.mark.order(13)
def test_13_user_register():
    res = requests.post(f"{BASE}/api/v1/users/register", json={
        "name": "Abhi",
        "email": "abhi@gmail.com",
        "password": "1234"
    })
    assert res.status_code == 201


@pytest.mark.order(14)
def test_14_search_restaurant():
    res = requests.get(f"{BASE}/api/v1/restaurants/search?name=Food")
    assert res.status_code == 200