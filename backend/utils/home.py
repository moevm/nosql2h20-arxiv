from flask_restful import reqparse, abort, Resource,request
from flask import jsonify, make_response, send_file
from .database_requester import DatabaseRequester

class Home(Resource):
    def get(self):
        print('export')
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        print('kek')
        req.export_database()
        return send_file('export.zip', as_attachment=True)


    def post(self):
        req = DatabaseRequester("bolt://localhost:7687", "neo4j", "password")
        print('import')
        print(request.files)
        try:
            filename = list(request.files)[0]
        except IndexError:
            return make_response( jsonify({'status': 'error'}),505)
        file = request.files[filename]
        data = file.read()
        print('fileName - ' + filename)
        file.save(filename)
        res = req.import_database(file)
        if res is None:
            return make_response( jsonify({'status': 'ok'}), 201)
        else:
            return make_response( jsonify({'status': 'error'}),505)
