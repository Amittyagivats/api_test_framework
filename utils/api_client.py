import requests
from config.config import BASE_URL, HEADERS

class APIClient:
    def __init__(self, base_url = BASE_URL, headers = HEADERS):
        self.base_url = base_url
        self.headers = headers
        
    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}/{endpoint}", headers=self.headers, params=params)
    
    def post(self, endpoint, payload=None):
        return requests.post(f"{self.base_url}/{endpoint}", headers=self.headers, json=payload  )
    
    def put(self, endpoint, payload=None):
        return requests.put(f"{self.base_url}/{endpoint}", headers=self.headers, json=payload)
    
    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}/{endpoint}", headers=self.headers)
    
    def graphql(self, query, variables=None):
        payload = {"query": query, "variables": variables or {}}
        return requests.post(self.base_url, headers=self.headers, json=payload)