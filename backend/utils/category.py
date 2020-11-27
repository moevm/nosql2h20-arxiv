from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('category', location='args')

def get_category(category,req):
    answer = [{
    'id':12,'category_name':'Biology','author_name':'Xu','article_name':'Sliding-Window QPS (SW-QPS): A Perfect Parallel Iterative Switching\n Algorithm for Input-Queued Switches'
    }]
    return answer

class Category(Resource):

    def get(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        args = parser.parse_args()
        print(args)
        category = args.get('category')
        answer = get_category(category,req)
        return make_response(
            jsonify(answer),
            200)
