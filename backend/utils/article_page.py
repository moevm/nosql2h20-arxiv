from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('article_page',location='args')

def get_article_page(article_page,req):
    answer = [
        {'id': '1', 'article_name': 'Sliding-Window QPS (SW-QPS): A Perfect Parallel Iterative Switching\n Algorithm for Input-Queued Switches', 'author_name': 'Xu','doi':123,'abstract':'abstract of this article'}
    ]
    return answer

class Article_page(Resource):
    def get(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        args = parser.parse_args()
        print(args)
        article_page = args.get('article_page')
        answer = get_article_page(article_page,req)
        return make_response(
            jsonify(answer),
            200)
