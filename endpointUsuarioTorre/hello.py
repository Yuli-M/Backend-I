from flask import Flask, request, jsonify
from queryUsuarios import usuarios_query, torre_query

app = Flask(__name__)

@app.route("/pagina")
def hello_world():

     return "<p>Paginaaa</p>"
 
@app.route("/echo", methods=["POST"])
def echo():

    name = request.values.get("name")
    to_echo = request.values.get("echo")

    response = "Hey there {}! You said {}".format(name, to_echo)

    return response


@app.route("/usuarios", methods=["GET"])
def usuarios():
    query = usuarios_query()
    return jsonify(query), 200

@app.route("/usuarios/<int:torre_id>", methods=["GET"])
def user_torre(torre_id):
    torre = torre_query(torre_id)
    return jsonify(torre), 200

app.run()
