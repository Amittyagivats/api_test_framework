from locust import HttpUser, task, between

class UserAPIUser(HttpUser):
    host = "http://localhost:8089"
    wait_time = between(1, 3)

    @task
    def get_users(self):
        self.client.get("/api/users")