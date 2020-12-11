from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('co_author', location='args')

def get_co_author(co_authors,req):
    name = req.get_authors_names([int(co_authors)])
    print(name)
    ids_of_co_authors = req.get_colleagues_of_author(int(co_authors))
    print(ids_of_co_authors)
    names_of_co_authors = req.get_authors_names(ids_of_co_authors)
    result=[]
    for author_name,author_id in zip(names_of_co_authors,ids_of_co_authors):
        result.append({'author_name':author_name,'author_id':author_id})
    print(result)
    answer=[{
    'author_name':name,
    'author_id':co_authors,
    'co_authors':result
    }]

    return answer

class CoAuthors(Resource):

    def get(self):
        req = DatabaseRequester("bolt://arxiv_neo4j:7687", "neo4j", "password")
        args = parser.parse_args()
        print(args)
        co_authors = args.get('co_author')
        answer = get_co_author(co_authors,req)
        return make_response(
            jsonify(answer),
            200)
