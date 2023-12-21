from flask import Flask, request, jsonify

app = Flask(__name__)



# Datos de ejemplo 
personas = [
    {"id": 1, "nombre": "Juan", "edad": 25},
    {"id": 2, "nombre": "Maria", "edad": 30},
    {"id": 3, "nombre": "Carlos", "edad": 28},
]


# Ruta para obtener todas las personas
@app.route('/personas', methods=['GET'])
def obtener_personas():
    return jsonify({"personas": personas})

# Ruta para obtener una persona por ID
@app.route('/personas/<int:id>', methods=['GET'])
def obtener_persona(id):
    persona = next((p for p in personas if p['id'] == id), None)
    if persona:
        return jsonify({"persona": persona})
    else:
        return jsonify({"mensaje": "Persona no encontrada"}), 404

# Ruta para agregar una nueva persona
@app.route('/personas', methods=['POST'])
def agregar_persona():
    nueva_persona = request.get_json()
    nueva_persona["id"] = len(personas) + 1
    personas.append(nueva_persona)
    return jsonify({"mensaje": "Persona agregada exitosamente", "persona": nueva_persona})


# Ruta para actualizar una persona por ID
@app.route('/personas/<int:id>', methods=['PUT'])
def actualizar_persona(id):
    persona_actualizada = request.get_json()
    for persona in personas:
        if persona['id'] == id:
            persona.update(persona_actualizada)
            return jsonify({"mensaje": "Persona actualizada exitosamente", "persona": persona})
    return jsonify({"mensaje": "Persona no encontrada"}), 404



# Ruta para eliminar una persona por ID
@app.route('/personas/<int:id>', methods=['DELETE'])
def eliminar_persona(id):
    global personas
    personas = [p for p in personas if p['id'] != id]
    return jsonify({"mensaje": "Persona eliminada exitosamente"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

