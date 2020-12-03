from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api
from ..controller.ferramentas_dao import FerramentaDAO as dao

ns = api.namespace('Ferramenta','Retorna todas as ferramentas')

@ns.route("/")
class FerramentaService(Resource):

    def get(self):
        ''' Retorna todas as ferramentas '''
        return make_response(
            jsonify({'resultado': dao().get_all()})
        )