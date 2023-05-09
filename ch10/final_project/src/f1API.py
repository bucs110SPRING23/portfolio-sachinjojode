import requests

class ErgastAPI:
    def __init__(self):
        self.api_url = "https://ergast.com/api/f1"

    def get_race_schedule(self, season):
        url = f"{self.api_url}/{season}.json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return data
