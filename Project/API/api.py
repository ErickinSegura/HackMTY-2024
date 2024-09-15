from flask import Flask, request, jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.prompter import Prompt
from DB.db import DB

# Crear Flask
app = Flask(__name__)

# Crear Prompter
ai = Prompt()

# Crear DB
db = DB()

# Definir la ruta principal
@app.route('/')
def hello_world():
    return 'Si, funciona!'

# Definir la ruta /prompt
@app.route('/prompt', methods=['POST'])
def echo():
    # Obtener el cuerpo de la solicitud
    data = request.json

    # Obtener el prompt y la seleccion
    prompt = data['prompt']
    selection = data['selection']

    # Obtener la respuesta
    response = ai.prompt(prompt, selection)
    return response

@app.route('/resume/<int:product_id>', methods=['GET'])
def get_resume(product_id):
    comentarios = db.get_comments_from_product(product_id)
    # Decodificar los textos

    return jsonify(comentarios)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
