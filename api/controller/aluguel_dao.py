from flask import jsonify, make_response
from ..model.aluguel import Aluguel, AluguelSchema
from .. import db

class AluguelDAO():

    def add(self,dados):
        try:
            obj = Aluguel()
            obj.modelo = dados.get('modelo')
            obj.tipo = dados.get('tipo')
            obj.marca = dados.get('marca')
            obj.preco = dados.get('preco')
            obj.cliente = dados.get('cliente')
            obj.telcli = dados.get('telcli')

            db.session.add(obj)
            db.session.commit()

            return make_response(jsonify({'mensagem: ': 'operacao realizada com sucesso'}),200)
        except Exception as err:
            return make_response(jsonify({'erro: ': '{0}'.format(err)}), 406)

    def update(self,dados):
        try:
            obj = Aluguel.query.filter(Aluguel.id==dados.get('id')).one()
            if obj is None:
                return make_response(jsonify({'erro: ': 'registro nao encontrado'}), 406)

            obj.modelo = dados.get('modelo')
            obj.tipo = dados.get('tipo')
            obj.marca = dados.get('marca')
            obj.preco = dados.get('preco')
            obj.cliente = dados.get('cliente')
            obj.telcli = dados.get('telcli')
            
            db.session.merge(obj)
            db.session.commit()

            return make_response(jsonify({'mensagem: ': 'operacao realizada com sucesso'}),200)
        except Exception as err:
            return make_response(jsonify({'erro: ': '{0}'.format(err)}), 406)


    def get_by_id(self,id):
        return AluguelSchema().dump(Aluguel.query.filter(Aluguel.id==id).one())

    def delete(self,id):
        try:
            Aluguel.query.filter(Aluguel.id==id).delete()
            db.session.commit()

            return make_response(jsonify({'mensagem: ': 'operacao realizada com sucesso'}),200)
        except Exception as err:
            return make_response(jsonify({'erro: ': '{0}'.format(err)}), 406)
