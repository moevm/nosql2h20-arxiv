from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester

parser = reqparse.RequestParser()
parser.add_argument('author', location='args')
data = {
    'labels': [
        'Red',
        'Green',
        'Yellow'
    ],
    'datasets': [{
        'data': [300, 50, 100],
        'backgroundColor': [
            '#FF6384',
            '#36A2EB',
            '#FFCE56'
        ],
        'hoverBackgroundColor': [
            '#FF6384',
            '#36A2EB',
            '#FFCE56'
        ]
    }]
}

bar_data = {
    'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    'datasets': [
        {
            'label': 'Authors',
            'data': [12, 19, 3, 5, 10, 3],
            'backgroundColor':[
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
            ],
            'borderColor': [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
            ],
            'borderWidth': 1,
        },
    ],
}

#def get_author(author,req):
#    retrun []

class Stat(Resource):

    def get(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")

        return make_response(
            jsonify(data,bar_data),
            200)
