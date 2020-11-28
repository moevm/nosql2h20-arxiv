from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('author_page',location='args')

def get_author(author_id,req):

    print(type(author_id))
    author_name = req.get_authors_names([int(author_id)])
    print(author_name)
    new_ids = req.get_author_articles_ids([int(author_id)])
    author_ids = [i[0] for i in new_ids]
    article_ids = [i[1] for i in new_ids]
    info = req.get_article_info(article_ids)
    print(info)
    articles=[]
    for ar_names,article_id in zip(info,article_ids):
        articles.append(
        {'article_id': article_id,'article_name': ar_names[0]}
        )
    answer = [{
        "author_name":author_name,
        'author_id':author_id,
        "articles":articles
        }]
    return answer

class Author_page(Resource):

    def get(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        args = parser.parse_args()
        print(args)
        author_page = args.get('author_page')
        print(author_page)
        answer = get_author(author_page,req)
        return make_response(
            jsonify(answer),
            200)
