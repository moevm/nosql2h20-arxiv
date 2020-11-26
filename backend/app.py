from flask import Flask
from flask_restful import Api
from utils.author import Author
from utils.author_page import Author_page
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Author, '/author')
api.add_resource(Author_page, '/author_page')

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)