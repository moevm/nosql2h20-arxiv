from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('author', location='args')

def get_author(author,req):
    answer = []
    ids = req.get_authors_ids(author)
    print(ids)
    if len(ids)==0:
        answer = [
        ]
        return answer
    names = req.get_authors_names(ids)
    new_ids = req.get_author_articles_ids(ids)
    author_ids = [i[0] for i in new_ids]
    article_ids = [i[1] for i in new_ids]
    if len(new_ids)==0:
        answer = [
        ]
        return answer
    info = req.get_article_info(article_ids)
    print(info)
    for id,article_id, ar_names in zip(author_ids,article_ids, info):
        answer.append({'id': id, 'name': names[ids.index(id)], 'article': ar_names[0],"article_id":article_id})
    return answer

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
