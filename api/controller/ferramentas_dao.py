from flask import jsonify, make_response
from ..model.ferramentas import Ferramenta, FerramentaSchema
from .. import db

class FerramentaDAO():

    def get_all(self):
        return FerramentaSchema().dump(Ferramenta.query.all(), many=True)
