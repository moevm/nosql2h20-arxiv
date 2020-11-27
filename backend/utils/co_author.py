from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('co_authors', location='args')

def get_co_author(co_authors,req):
    answer = [{
        "author_name":co_authors,
        'co_authors':[
        "Amir",
        "Marlen",
        "Kate"
        ]
    }]

    return answer

class CoAuthors(Resource):

    def get(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        args = parser.parse_args()
        print(args)
        co_authors = args.get('co_authors')
        answer = get_co_author(co_authors,req)
        return make_response(
            jsonify(answer),
            200)
