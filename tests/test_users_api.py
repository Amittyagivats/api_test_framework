import pytest
import requests
import json
from utils.api_client import APIClient
from utils.assertions import assert_status_code, assert_json_key
from utils.schema_validator import validate_schema

client = APIClient()

def test_get_users():
    response = client.get("users")
    assert_status_code(response, 200)
    assert_json_key(response, "data")

def test_get_user_by_id():
    response = client.get("users/2")
    assert_status_code(response, 200)
    assert response.json()["data"]["id"] == 2

def test_create_user():
    payload = {"name": "Sam Kumar", "job": "QA Engineer"}
    response = client.post("users", payload)
    assert_status_code(response, 201)
    assert_json_key(response, "id")

def test_update_user():
    payload = {"name": "Sam Updated", "job": "Senior QA"}
    response = client.put("users/2", payload)
    assert_status_code(response, 200)
    assert response.json()["name"] == "Sam Updated"

def test_delete_user():
    response = client.delete("users/2")
    assert_status_code(response, 204)

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id_param(user_id):
    response = client.get(f"users/{user_id}")
    assert_status_code(response, 200)
    assert response.json()["data"]["id"] == user_id

def test_user_list_schema():
    schema = {
        "type": "object",
        "properties": {
            "page": {"type": "integer"},
            "data": {"type": "array"}
        },
        "required": ["page", "data"]
    }
    response = client.get("users")
    assert_status_code(response, 200)
    validate_schema(response.json(), schema)

@pytest.mark.parametrize("user", json.load(open("data/users.json")))
def test_create_user_from_json(user):
    response = client.post("users", user)
    assert_status_code(response, 201)
    assert response.json()["name"] == user["name"]
    
    
def test_graphql_country_query():
    query = """
    query {
      country(code: "IN") {
        name
        capital
        currency
      }
    }
    """
    payload = {"query": query}
    response = requests.post("https://countries.trevorblades.com", json=payload)
    assert response.status_code == 200
    assert "data" in response.json()
    assert response.json()["data"]["country"]["name"] == "India"