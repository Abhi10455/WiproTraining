import requests
import pytest

BASE = "http://127.0.0.1:5000"


@pytest.mark.order(15)
def test_15_place_order():
    res = requests.post(f"{BASE}/api/v1/orders", json={
        "user_id": 1,
        "restaurant_id": 1,
        "dish": "Paneer"
    })
    assert res.status_code == 201


@pytest.mark.order(16)
def test_16_rating():
    res = requests.post(f"{BASE}/api/v1/ratings", json={
        "order_id": 1,
        "rating": 5,
        "comment": "Good"
    })
    assert res.status_code == 201


@pytest.mark.order(17)
def test_17_orders_by_restaurant():
    res = requests.get(f"{BASE}/api/v1/restaurants/1/orders")
    assert res.status_code == 200


@pytest.mark.order(18)
def test_18_orders_by_user():
    res = requests.get(f"{BASE}/api/v1/users/1/orders")
    assert res.status_code == 200