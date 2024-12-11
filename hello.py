from flask import Flask, request, jsonify, session, redirect, url_for
from queryUsuarios import usuarios_query, torre_query

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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

# manejo de sesiones
@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


app.run()
