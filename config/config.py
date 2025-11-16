import os

ENV = os.getenv("ENV", "dev")

CONFIG = {
    "dev": {
        "base_url": "https://reqres.in/api",
        "headers": {
            "x-api-key": "reqres-free-v1",
            "Content-Type": "application/json"
        }
    }
}

BASE_URL = CONFIG[ENV]["base_url"]
HEADERS = CONFIG[ENV]["headers"]