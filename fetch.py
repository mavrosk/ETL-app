import requests
from datetime import datetime


class Fetcher:
    BASE_URL = "https://openexchangerates.org/api/"
    API_KEY = "56251d0eafd4475dab803ed1ac1aca8f"

    @staticmethod
    def fetch_data(date):
        url = f"{Fetcher.BASE_URL}latest.json?app_id={Fetcher.API_KEY}"
        
        headers = {"accept": "application/json"}
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        return response.json()
    
