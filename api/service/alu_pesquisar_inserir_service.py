from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api
from ..controller.aluguel_dao import AluguelDAO as dao

ns = api.namespace('aluguelpequisarinserir', 'Aluguel')


@ns.route("/")
class AluguelInserirrService(Resource):

    def post(self):
        ''' Adicionar um novo aluguel '''
        if self.api.payload is None:
            return make_response(jsonify({'erro': 'conteudo invalido'}), 406)
        return dao().add(self.api.payload)

@ns.route("/<id>")
class AluguelServiceItem(Resource):

    def get(self, id):
        ''' Retornar dados de um Aluguel a partir do Id'''
        return make_response(
            jsonify({'resultado' : dao().get_by_id(id)})
        ) 

