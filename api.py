from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from models import Note
from resources import *

app = Flask(__name__)
api = Api(app)

## Actually setup the API resource routing

api.add_resource(NoteListResource, '/notes/', endpoint='notes')
api.add_resource(NoteResource, '/notes/<string:id>', endpoint='note')


if __name__ == '__main__':
    app.run(debug=True)