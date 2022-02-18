from unittest import result
from flask import Flask, render_template, jsonify, request
import module
from flask_cors import CORS


# Created a class object
object = module.Test()

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST'])
def hello_world():
    data = request.get_json()
    passw = data['pass']
    a = object.lis(passw)
    passww = object.hash(a)
    return jsonify({"passw": passww})


@app.route("/1/<string:ooo>",)
def ok(ooo):
    a = object.lis(ooo)
    room_no = object.hash(a)
    return jsonify(room_no)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
