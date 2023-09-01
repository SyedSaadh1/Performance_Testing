from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Wait between 1 and 5 seconds

    @task
    def get_weather(self):
        headers = {"API-Key": "YOUR_OPENWEATHERMAP_API_KEY"}  # Replace with your API key
        self.client.get("/data/2.5/weather?q=London,uk", headers=headers)
