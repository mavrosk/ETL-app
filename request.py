import requests
from datetime import datetime

now = datetime.now()
current_date = now.date()

url = "https://openexchangerates.org/api/latest.json?app_id=56251d0eafd4475dab803ed1ac1aca8f"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)



print(response.text)