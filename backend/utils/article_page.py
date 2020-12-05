from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('article_page',location='args')

def get_article_page(article_page,req):
    answer =[]
    print(article_page)
    if article_page == '':
        return [{}]
    article_info = req.get_article_info([int(article_page)])
    author_info = req.get_article_authors_ids([int(article_page)])
    author_id = [i[0] for i in author_info]
    author_name = [i[1] for i in author_info]
    print(author_name)
    print(author_id)
    print(article_info)
    authors = []
    if article_info[0][1] == '':
        article_info[0][1] = ' '
    for name,id in zip(author_name,author_id):
        authors.append({'author_name':name,'author_id':id})
    answer = [{
            'article_name':article_info[0][0],
            'authors_info': authors,
            'doi':article_info[0][1],
            'category':article_info[0][2],
            'abstract':article_info[0][3]
        }]
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
