import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

taos = {}
with open("formatted_tao.txt") as g:
    t = g.read().splitlines()
    for a, b in enumerate(t):
        taos[a]=b



@app.route('/', methods=["GET"])
def home():
    return("<h1>welcome to my API</h1>")

@app.route('/api/all', methods=["GET"])
def api_all():
    return(taos)

@app.route('/api/pick', methods=["GET"])
def api_id():
    id = int(request.args.get('id'))
    return(taos[id])

app.run()