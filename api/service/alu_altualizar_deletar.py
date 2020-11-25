from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api
from ..controller.aluguel_dao import AluguelDAO as dao

ns = api.namespace('aluguelatualizardeletar', 'Aluguel')


@ns.route("/")
class AluguelAtualizarDeletarService(Resource):

    def put(self):
        ''' Atualizar dados do Aluguel '''
        if self.api.payload is None:
            return make_response(jsonify({'erro': 'conteudo invalido'}), 406)
        return dao().update(self.api.payload)

    def delete(self):
        ''' Deletar dados do aluguel '''
        if self.api.payload is None:
            return make_response(jsonify({'erro': 'conteudo invalido'}), 406)
        return dao().update(self.api.payload)



