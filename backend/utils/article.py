from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('article', location='args')

def get_article(article,req):
    answer = [
                {'id': '1', 'article_name': 'Sliding-Window QPS (SW-QPS): A Perfect Parallel Iterative Switching\n Algorithm for Input-Queued Switches', 'author_name': 'Xu'}
            ]
    '''article_ids = req.get_article_ids(author)
    if len(ids)==0:
        answer = [
            #{'id': 'loading...', 'name': 'loading...', 'article': 'loading...'}
        ]
        return answer
    article_names = req.get_article_names(ids)
    if len(names)==0:
        answer = [
            #{'id': 'loading...', 'name': 'loading...', 'article': 'loading...'}
        ]
        return answer
    auhtors = req.get_author_names(article_ids,article_names)
    for id, ar_names,author in zip(author_ids, info,auhtors):
        answer.append({'id': id, 'name': names[ids.index(id)], 'article': ar_names[0]})'''
    return answer

class Article(Resource):

    def get(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        args = parser.parse_args()
        print(args)
        article = args.get('article')
        answer = get_article(article,req)
        return make_response(
            jsonify(answer),
            200)
