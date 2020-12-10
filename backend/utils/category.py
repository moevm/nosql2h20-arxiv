from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('category', location='args')

def get_category(category,req):
    answer = []
    if category == '':
        return answer
    print(category)
    articles = req.get_articles_by_category(category)
    print(len(articles))
    articles_info = req.get_article_info(articles)
    author_names = req.get_article_authors_ids(articles)
    for article,article_info,author in zip(articles,articles_info,author_names):
        answer.append({'article_name':article_info[0],'article_id':article,'author_name':author[1],'author_id':author[0],'category':article_info[2]})
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
