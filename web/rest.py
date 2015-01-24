#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g, Response, request, session, jsonify
from flask.ext.restful import Resource, reqparse

from web import api


class ScoreAPI(Resource):
    """
    Defines a RESTful API for Article elements.
    """
    #method_decorators = [authenticate]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(ScoreAPI, self).__init__()

    def get(self):
        """
        Returns a list of articles.
        """
        return jsonify(result= {
                                    "score": 10,
                                    "nic": "John",
                                    "avatar": "m111"
                                }
                        )
api.add_resource(ScoreAPI, '/api/v1/scores', endpoint = 'scores.json')