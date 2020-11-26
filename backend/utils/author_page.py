from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('author_page',location='args')

def get_author(author,req):
    answer = []
    ids = req.get_authors_ids(author)
    if len(ids)==0:
        answer = [
            {'id': 'loading...', 'name': 'loading...', 'article': 'loading...'}
        ]
        return answer
    names = req.get_authors_names(ids)
    new_ids = req.get_author_articles_ids(ids)
    author_ids = [i[0] for i in new_ids]
    article_ids = [i[1] for i in new_ids]
    if len(new_ids)==0:
        answer = [
            {'id': 'loading...', 'name': 'loading...', 'article': 'loading...'}
        ]
        return answer
    info = req.get_article_info(article_ids)
    print(info)
    for id, ar_names in zip(author_ids, info):
        answer.append({'id': id, 'name': names[ids.index(id)], 'article': ar_names[0]})
    return answer

class Author_page(Resource):

    def get(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        args = parser.parse_args()
        print(args)
        author = args.get('author')
        author_page = args.get('author_page')
        print(author_page)
        answer = get_author(author_page,req)
        return make_response(
            jsonify(answer),
            200)