from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from werkzeug.wrappers import response

# Inisiasi object flask
app = Flask(__name__)


# Inisiasi object flask_restful
api = Api(app)

# Inisiasi object flask_cors
CORS(app)

# inisiasi variable kosong
user = {}


# membuat class Resource
class ContohResource(Resource):
    # methode get dan post
    def get(self):
        # response = {"msg": "Hallo World!"}
        return user

    def post(self):
        name = request.form["name"]
        age = request.form["age"]
        user["name"] = name
        user['age'] = age
        res = {"msg": "Berhasil Menambah Data User"}
        return res


# setup resourcenya
api.add_resource(ContohResource, "/api", methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
