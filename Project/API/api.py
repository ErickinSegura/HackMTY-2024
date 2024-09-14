from flask import Flask, request, jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.prompter import Prompt

# Crear Flask
app = Flask(__name__)

# Crear Prompter
ai = Prompt()

# Definir la ruta principal
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Definir la ruta /echo
@app.route('/echo', methods=['POST'])
def echo():
    # Obtener el cuerpo de la solicitud
    data = request.json

    # Obtener el prompt y la seleccion
    prompt = data['prompt']
    selection = data['selection']

    # Obtener la respuesta
    response = ai.prompt(prompt, selection)
    return response

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
