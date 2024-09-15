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
    
    #Quitar sublistas
    comentarios = [comentario[0] for comentario in comentarios]

    return jsonify(comentarios)

@app.route('/best_comments/<int:product_id>', methods=['GET'])
def get_best_comments(product_id):
    comentarios = db.get_comments_from_product(product_id)
    comentarios = str(comentarios) + " 2"
    response = ai.prompt(comentarios, 3)
    response = eval(response)
    return jsonify(response)

@app.route('/worst_comments/<int:product_id>', methods=['GET'])
def get_worst_comments(product_id):
    comentarios = db.get_comments_from_product(product_id)
    comentarios = str(comentarios) + " 3"
    response = ai.prompt(comentarios, 3)
    response = eval(response)
    return jsonify(response)

@app.route('/op_general/<int:product_id>', methods=['GET'])
def get_general_opinion(product_id):
    comentarios = db.get_comments_from_product(product_id)
    comentarios = str(comentarios) + " 1"
    response = ai.prompt(comentarios, 3)
    return jsonify(response)

@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.json.get('prompt')

    # Obtener la respuesta
    response = ai.prompt(prompt, 1)
    result = db.run_query(response)
    analysis = ai.prompt(str(prompt) + " " + str(response) + " " + str(result), 4)

    return jsonify(analysis)

@app.route('/products', methods=['GET'])
def get_products():
    result = db.run_query("SELECT nombre FROM productos")
    results = [row[0] for row in result]
    return jsonify(results)

@app.route('/opinion', methods=['POST'])
def opinion():
    data = request.json
    opinion = data['opinion']
    product = data['product']

    # Ejecutar la consulta usando parámetros para evitar inyección SQL
    print(f"CALL crear_comentario('{product}', '{opinion}')")
    db.add_comment(product, opinion)

    return jsonify({"status": "success", "message": "Comentario agregado correctamente"})



# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
