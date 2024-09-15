from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.prompter import Prompt
from DB.db import DB

# Crear Flask
app = Flask(__name__)
CORS(app)

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

@app.route('/best_comments/<string:product_name>', methods=['GET'])
def get_best_comments(product_name):
    comentarios = db.get_comments_from_name(product_name)
    comentarios = str(comentarios) + " 2"
    response = ai.prompt(comentarios, 3)
    response = eval(response)
    return jsonify(response)

@app.route('/worst_comments/<string:product_name>', methods=['GET'])
def get_worst_comments(product_name):
    comentarios = db.get_comments_from_name(product_name)
    comentarios = str(comentarios) + " 3"
    response = ai.prompt(comentarios, 3)
    response = eval(response)
    return jsonify(response)

@app.route('/op_general/<string:product_name>', methods=['GET'])
def get_general_opinion(product_name):
    comentarios = db.get_comments_from_name(product_name)
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

    product_id_query = f"SELECT id_producto FROM productos WHERE nombre = '{product}'"
    product_id = db.run_query(product_id_query)[0][0]

    # Ejecutar la consulta usando parámetros para evitar inyección SQL
    print(f"CALL crear_comentario('{product}', '{opinion}')")
    db.add_comment(product, opinion)

    result = eval(ai.prompt(opinion, 2))
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
        db.insert_opinion(product_id, cat, opinion[1])

    return jsonify({"status": "success", "message": "Comentario agregado correctamente"})

@app.route('/comments/<string:product_name>', methods=['GET'])
def get_comments(product_name):
    print(f"Buscando comentarios para el producto: {product_name}")
    comentarios = db.get_comments_from_name(product_name)
    comentarios = [comentario[0] for comentario in comentarios]
    return jsonify(comentarios)

@app.route('/start', methods=['GET'])
def start():
    # Restart opiniones
    db.run_query("DELETE FROM opinion")

    products = db.run_query("SELECT nombre FROM productos")
    products = [product[0] for product in products]

    for product in products:

        product_id_query = f"SELECT id_producto FROM productos WHERE nombre = '{product}'"
        product_id = db.run_query(product_id_query)[0][0]

        comentarios = db.get_comments_from_name(product)
        comentarios = [comentario[0] for comentario in comentarios]

        for comentario in comentarios:
            result = eval(ai.prompt(comentario, 2))
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
    return jsonify({"status": "success", "message": "Proceso completado"})

@app.route('/get_score/<string:product_name>/<int:category>', methods=['GET'])
def get_score(product_name, category):
    score = db.get_score(product_name, category)
    return jsonify({"score": score})

@app.route('/review/<string:product_name>/<int:category>', methods=['GET'])
def get_review(product_name, category):
    scores = db.get_scores(product_name)
    prompt = "Producto: " + str(product_name) + str(scores) + str(category)
    response = ai.prompt(prompt, 5)
    return jsonify(response)


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
