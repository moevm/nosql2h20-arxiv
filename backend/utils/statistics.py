from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('author', location='args')

def get_author(author,req):
    retrun []

class Author(Resource):

    def get(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        args = parser.parse_args()
        print(args)
        author = args.get('author')
        answer = get_author(author,req)
        return make_response(
            jsonify(answer),
            200)
