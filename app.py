from flask import Flask, request, jsonify
import os
from pymongo import MongoClient
from bson import ObjectId  
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

try:
    # Intentar crear la conexión a MongoDB
    client = MongoClient(mongo_uri)
    db = client["json"]
    collection = db["json"]
    print("Conexión a MongoDB establecida correctamente.")
except Exception as e:
    print(f"Error al conectar a MongoDB: {e}")

app = Flask(__name__)

# Ruta para obtener todas las personas
@app.route('/personas', methods=['GET'])
def obtener_personas():
    personas = list(collection.find())
    for persona in personas:
        persona['_id'] = str(persona['_id'])
    return jsonify({"personas": personas})

# Ruta para obtener una persona por ID
@app.route('/personas/<int:id>', methods=['GET'])
def obtener_persona(id):
    persona = collection.find_one({"id": id})
    if persona:
        # Convierte ObjectId a cadena para hacerlo serializable a JSON
        persona['_id'] = str(persona['_id'])
        return jsonify({"persona": persona})
    else:
        return jsonify({"mensaje": "Persona no encontrada"}), 404

# Ruta para agregar una nueva persona
@app.route('/personas', methods=['POST'])
def agregar_persona():
    nueva_persona = request.get_json()
    result = collection.insert_one(nueva_persona)
    nueva_persona["_id"] = str(result.inserted_id)
    return jsonify({"mensaje": "Persona agregada exitosamente", "persona": nueva_persona})

# Ruta para actualizar una persona por ID
@app.route('/personas/<string:_id>', methods=['PUT'])
def actualizar_persona(_id):
    persona_actualizada = request.get_json()
    result = collection.update_one({"_id": ObjectId(_id)}, {"$set": persona_actualizada})
    
    if result.modified_count > 0:
        return jsonify({"mensaje": "Persona actualizada exitosamente", "persona": persona_actualizada})
    else:
        return jsonify({"mensaje": "Persona no encontrada"}), 404

# Ruta para eliminar una persona por ID
@app.route('/personas/<string:_id>', methods=['DELETE'])
def eliminar_persona(_id):
    result = collection.delete_one({"_id": ObjectId(_id)})
    
    if result.deleted_count > 0:
        return jsonify({"mensaje": "Persona eliminada exitosamente"})
    else:
        return jsonify({"mensaje": "Persona no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
