from Model.prompter import Prompt
from DB.db import DB
import requests
import json

pr = Prompt()
db = DB()

result = db.get_scores("bicicleta")
prompt = "Producto: bicicleta " + str(result) + " 2"
response = pr.prompt(prompt, 5)
print(response)