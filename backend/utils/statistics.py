from flask_restful import reqparse, abort, Resource
from flask import jsonify, make_response
from .database_requester import DatabaseRequester
import random as rdm
parser = reqparse.RequestParser()
parser.add_argument('author', location='args')


def get_category_stat(req):
    stat = req.get_categories_statistics()
    labels = []
    stat_data = []
    color = []
    for par in stat:
        labels.append(par[0])
        stat_data.append(par[1])
    print(labels)
    print(stat_data)
    for i in range(len(stat_data)):
        color.append([
            'rgba({},{},{}, 1)'.format(rdm.randint(0,255),rdm.randint(0,255),rdm.randint(0,255))
        ])
    return {
                 'labels': labels,
                 'datasets': [{
                    'label':'Categories',
                     'data': stat_data,
                     'backgroundColor': color
                 }]
             }

def get_get_authors_stat(req):
    stat = req.get_authors_statistics()
    labels = []
    stat_data = []
    color = []
    for par in stat:
        labels.append(par[0])
        stat_data.append(par[1])
    print(labels)
    print(stat_data)
    names = req.get_authors_names(labels)
    for i in range(len(stat_data)):
        color.append([
            'rgba({},{},{}, 1)'.format(rdm.randint(0,255),rdm.randint(0,255),rdm.randint(0,255))
        ])
    return {
                 'labels': names,
                 'datasets': [{
                     'data': stat_data,
                     'backgroundColor': color
                 }]
             }
class Stat(Resource):
    def get(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        bar_data = get_category_stat(req)
        data = get_get_authors_stat(req)
        return make_response(
            jsonify(data,bar_data),
            200)
