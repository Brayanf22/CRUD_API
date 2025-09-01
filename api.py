from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def root():
    return"Hola mundo"

'''
GET -> obtener informacion
POST -> Crear informacion
PUT -> Actualizar informacion
DELETE -> Borrar informacion
'''
"Metodo GET"
@app.route("/user/<user_id>")
def get_user(user_id):
    user={"id": user_id, "name":"test", "telefono":"99-666-333"}
    query = request.args.get("query")
    if query:
        user[query]=query
    return jsonify(user), 200

"Metodo POST"
@app.route('/user', methods=['POST'])
def creat_user():
    data = request.get_json()  # recibe JSON

    # Validación simple
    if not data or "name" not in data or "telefono" not in data:
        return jsonify({"error": "Faltan campos: name y telefono"}), 400

    # Simulación de creación de usuario
    user = {
        "id": 1,  # en un sistema real lo genera la BD
        "name": data["name"],
        "telefono": data["telefono"]
    }

    return jsonify({"mensaje": "Usuario creado con éxito", "usuario": user}), 201

"Metodo PUT"
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()  # recibe JSON

    # Validación simple
    if not data or "name" not in data or "telefono" not in data:
        return jsonify({"error": "Faltan campos: name y telefono"}), 400

    # Simulación de actualización
    user = {
        "id": user_id,
        "name": data["name"],
        "telefono": data["telefono"]
    }

    return jsonify({"mensaje": "Usuario actualizado con éxito", "usuario": user}), 200

"Metodo Delete"
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Simulación de eliminación
    return jsonify({"mensaje": f"Usuario con id {user_id} eliminado con éxito"}), 200


if __name__ == "__main__":
    app.run(debug=True)