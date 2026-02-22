import requests
import pytest

BASE = "http://127.0.0.1:5000"

DISH_ID = None


@pytest.mark.order(5)
def test_5_add_dish():
    global DISH_ID

    res = requests.post(f"{BASE}/api/v1/restaurants/1/dishes", json={
        "name": "Paneer",
        "price": 200
    })
    assert res.status_code == 201

    data = res.json()
    DISH_ID = data["id"]   # capture actual id


@pytest.mark.order(6)
def test_6_update_dish():
    res = requests.put(f"{BASE}/api/v1/dishes/{DISH_ID}", json={
        "price": 250
    })
    assert res.status_code == 200


@pytest.mark.order(7)
def test_7_disable_dish():
    res = requests.put(f"{BASE}/api/v1/dishes/{DISH_ID}/status", json={
        "enabled": False
    })
    assert res.status_code == 200


@pytest.mark.order(8)
def test_8_delete_dish():
    res = requests.delete(f"{BASE}/api/v1/dishes/{DISH_ID}")
    assert res.status_code == 200