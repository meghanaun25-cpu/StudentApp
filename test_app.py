from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Welcome to StudentApp!"


def test_about():
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200
    assert response.data == b"This is a Student Management Application."