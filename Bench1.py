import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("api_key")

playerID = '44067861'
base_url = 'https://www.opendota.com/players/{playerID}/heroes?patch=50&having=5'
endpoint = f"{base_url}?api_key={api_key}"
r = requests.get(endpoint)
print(r.json())