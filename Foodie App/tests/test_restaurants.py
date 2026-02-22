import requests
import pytest

BASE = "http://127.0.0.1:5000"


@pytest.mark.order(1)
def test_1_register_restaurant():
    res = requests.post(f"{BASE}/api/v1/restaurants", json={
        "name": "Food Hub",
        "category": "Veg",
        "location": "Hyderabad",
        "contact": "999999"
    })
    assert res.status_code == 201


@pytest.mark.order(2)
def test_2_update_restaurant():
    res = requests.put(f"{BASE}/api/v1/restaurants/1", json={
        "location": "Bangalore"
    })
    assert res.status_code == 200


@pytest.mark.order(3)
def test_3_disable_restaurant():
    res = requests.put(f"{BASE}/api/v1/restaurants/1/disable")
    assert res.status_code == 200


@pytest.mark.order(4)
def test_4_view_restaurant():
    res = requests.get(f"{BASE}/api/v1/restaurants/1")
    assert res.status_code == 200