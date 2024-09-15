# Correct usage of the Prompt class
from Model.prompter import Prompt
from DB.db import DB

import requests

pr = Prompt()

db = DB()


prom = "Por que las bicicletas se estan vendiendo tan mal"              

response = pr.prompt(prom, 1)

result = db.run_query(response)


analysis = pr.prompt(str(prom) + " " + str(response) + " " + str(result), 4)

print(analysis)


