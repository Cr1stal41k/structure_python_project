import random

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# Функция для генерации уникального номера телефона
def generate_unique_number():
    return str(random.randint(10000000000, 99999999999))


def test_create_person_api():
    unique_number = generate_unique_number()
    response = client.post("/v1/persons/persons/", json={"name": "John", "second_name": "Doe", "number": unique_number})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["second_name"] == "Doe"
    assert data["number"] == unique_number


def test_get_persons_api():
    response = client.get("/v1/persons/persons/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_persons_by_name_api():
    response = client.get("/v1/persons/persons/John")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "John"


def test_update_persons_by_id_api():
    response = client.get("/v1/persons/persons/")
    person_id = response.json()[0]["id"]
    update_data = {"name": "Jane", "second_name": "Doe", "number": generate_unique_number()}
    update_response = client.put(f"/v1/persons/persons/{person_id}", json=update_data)
    assert update_response.status_code == 200


def test_delete_persons_by_id_api():
    response = client.get("/v1/persons/persons/")
    person_id = response.json()[0]["id"]
    delete_response = client.delete(f"/v1/persons/persons/{person_id}")
    assert delete_response.status_code == 200
