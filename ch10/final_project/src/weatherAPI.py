import requests

class WeatherstackAPI:
    def __init__(self):
        self.api_url = "http://api.weatherstack.com"
        self.access_key = "13e3968b2a0cc2c6ead8dc4b1074fd59"

    def get_current_weather(self, location):
        url = f"{self.api_url}/current?access_key={self.access_key}&query={location}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data