from Model.prompter import Prompt
from DB.db import DB
import requests
import json

pr = Prompt()
db = DB()

url = 'https://redesigned-space-succotash-v9wv45jjqxw3pvpv-5000.app.github.dev/ask'
prom = "Por que las bicicletas se estan vendiendo tan mal" 

data = {"prompt": prom}

response = requests.post(url, json=data)
json_data = json.loads(response.text)
print(json_data)  