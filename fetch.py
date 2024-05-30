import requests
from datetime import datetime

class Fetcher:
    BASE_URL = "https://openexchangerates.org/api/historical/"
    API_KEY = "YOUR_API_KEY"

    def fetch_data(self, date):
        url = f"{self.BASE_URL}{date}.json?app_id={self.API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
