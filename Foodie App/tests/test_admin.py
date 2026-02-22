import requests
import pytest

BASE = "http://127.0.0.1:5000"


@pytest.mark.order(9)
def test_9_approve_restaurant():
    res = requests.put(f"{BASE}/api/v1/admin/restaurants/1/approve")
    assert res.status_code == 200


@pytest.mark.order(10)
def test_10_admin_disable():
    res = requests.put(f"{BASE}/api/v1/admin/restaurants/1/disable")
    assert res.status_code == 200


@pytest.mark.order(11)
def test_11_feedback():
    res = requests.get(f"{BASE}/api/v1/admin/feedback")
    assert res.status_code == 200


@pytest.mark.order(12)
def test_12_orders():
    res = requests.get(f"{BASE}/api/v1/admin/orders")
    assert res.status_code == 200