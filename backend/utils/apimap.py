from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response

parser = reqparse.RequestParser()
parser.add_argument('author', location='args')

class ApiMap(Resource):

    def get(self):
        args = parser.parse_args()
        author = args.get('author')
        answer=[]
        answer = [
            {'id':10,'name':author,'article':'new'},
        ]
        return make_response(
            jsonify(answer),
            200)