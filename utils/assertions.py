def assert_status_code(response, expected):
    assert response.status_code == expected, f"Expected status code {expected}, got {response.status_code}"
    
def assert_json_key(response, key):
    assert key in response.json(), f"Missing Key: '{key}' in response"
