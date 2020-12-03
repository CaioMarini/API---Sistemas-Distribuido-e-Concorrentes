from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api
from ..controller.aluguel_dao import AluguelDAO as dao

ns = api.namespace('Aluguel02', 'Atualizar e Deletar')


@ns.route("/")
class AluguelAtualizarDeletarService(Resource):

    def put(self):
        ''' Atualizar dados de um Aluguel '''
        if self.api.payload is None:
            return make_response(jsonify({'erro': 'conteudo invalido'}), 406)
        return dao().update(self.api.payload)


@ns.route("/<id>")
class AluguelDeletarService(Resource):

    def delete(self, id):
        ''' Deleta um aluguel a partir do Id'''
        return dao().delete(id) 



