from Model.prompter import Prompt
from DB.db import DB
import requests
import json

pr = Prompt()
db = DB()

comment = "La calidad de los materiales no es la mejor, pero el diseño es atractivo."
product = 'bicicleta'

# Get the product ID from the database
product_id_query = f"SELECT id_producto FROM productos WHERE nombre = '{product}'"
product_id = db.run_query(product_id_query)[0][0]
print(product_id)

# Get opinions
result = eval(pr.prompt(comment, 2))
for opinion in result:

    # Categorize the opinion
    if opinion[0] == "Tiempo de entrega":
        cat = 0
    elif opinion[0] == "Calidad de los materiales":
        cat = 1
    elif opinion[0] == "Comodidad de uso":
        cat = 2
    elif opinion[0] == "Estética":
        cat = 3
    elif opinion[0] == "Precio":
        cat = 4

    # Insert the opinion into the database
    db.insert_opinion(product_id, cat, opinion[1])  # Insert the opinion into the database