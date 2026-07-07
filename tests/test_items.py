def test_create_item(client):
    response = client.post(
        "/items",
        json={
            "name": "Test Hammer",
            "price": 9.99,
            "is_offer": False,
        },
        headers={"x-token": "secret-token"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Hammer"
    assert data["price"] == 9.99
    assert data["is_offer"] is False
    assert "id" in data
    assert "cost_price" not in data
    assert "created_by" not in data


def test_list_items(client):
    """先创建一条数据，再确认列表能查到它。"""
    client.post(
        "/items",
        json={"name": "Test Item", "price": 5.0},
        headers={"x-token": "secret-token"},
    )
    response = client.get("/items", headers={"x-token": "secret-token"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_read_item_not_found(client):
    response = client.get("/items/99999", headers={"x-token": "secret-token"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_missing_token_returns_401(client):
    response = client.get("/items")
    assert response.status_code == 401


def test_create_item_missing_name(client):
    response = client.post(
        "/items",
        json={"price": 9.99},
        headers={"x-token": "secret-token"},
    )
    assert response.status_code == 422
