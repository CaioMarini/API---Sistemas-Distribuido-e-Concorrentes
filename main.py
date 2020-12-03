from api import app, api, blueprint
from api.config import log
from api.service.ferramenta_service import ns as ns_ferramenta
from api.service.alu_pesquisar_inserir_service import ns as ns_aluguelpesq
from api.service.alu_atualizar_deletar_service import ns as ns_alugueldeleteup

api.init_app(blueprint)
app.register_blueprint(blueprint)

#REGISTRAR as rotas
api.add_namespace(ns_ferramenta)
api.add_namespace(ns_aluguelpesq)
api.add_namespace(ns_alugueldeleteup)


log.info('>> LIVRARIA API http://{}'.format(app.config['SERVER_NAME']))
app.run(debug=True)