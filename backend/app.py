from flask import Flask
from flask_restful import Api
from utils.author import Author
from utils.home import Home
from utils.co_author import CoAuthors
from utils.statistics import Stat
from utils.article import Article
from utils.category import Category
from utils.article_page import Article_page
from utils.author_page import Author_page
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Home, '/home')
api.add_resource(Author, '/author')
api.add_resource(CoAuthors, '/co_author')
api.add_resource(Author_page, '/author_page')
api.add_resource(Stat, '/statistics')
api.add_resource(Article, '/article')
api.add_resource(Article_page, '/article_page')
api.add_resource(Category, '/category')

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)