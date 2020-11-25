from flask import Flask
from flask_restful import Api
from utils.apimap import ApiMap
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(ApiMap, '/author')

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)