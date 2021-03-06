#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import render_template
import queries

"""
The api logic / routing runs here. Here the parameters and values are linked to
and passed on to the correct queries.
"""

app = Flask(__name__)
api = Api(app)

class Api(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            # make sure to set correct type in parser, for yiddish do not set string
            # parser defaults nicely to unicode, so do not set type for yiddish text
            parser.add_argument('vertaling', help='zoeken in vertaling')
            parser.add_argument('woord_zoek', help='zoeken in woord zonder diacrieten')
            parser.add_argument('q', help='zoeken in alles')
            parser.add_argument('id', help='zoeken op id')
            args = parser.parse_args()
            if args['vertaling']:
                _query = args['vertaling']
                qq = queries.queryVertalingContains(_query)
                return {'Query': args['vertaling'], 'IDs': qq}
            elif args['woord_zoek']:
                _query = args['woord_zoek']
                qq = queries.queryWoordZoekContains(_query)
                return {'Query': 'woord_zoek='+ args['woord_zoek'], 'IDs': qq}
            elif args['q']:
                _query = args['q']
                qq = queries.queryAllContains(_query)
                return {'Query': args['q'], 'IDs': qq}
            elif args['id']:
                return queries.queryID(args['id'])
            else:
                return {'Query':'Not implemented'}
        except Exception as e:
            return {'error': str(e)}

api.add_resource(Api, '/Api')

@app.route("/")
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)
