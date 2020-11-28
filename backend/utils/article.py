from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('article', location='args')

def get_article(article,req):
    answer = []
    if article == '':
        return answer
    articles_ids = req.get_articles_ids(article)
    info = req.get_article_info(articles_ids)
    for article_info,article_id in zip(info,articles_ids):
        answer.append({
            'article_id':article_id,
            'article_name':article_info[0]
        })
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
