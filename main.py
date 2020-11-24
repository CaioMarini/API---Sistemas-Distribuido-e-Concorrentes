from api import app, api, blueprint
from api.config import log
from api.service.ferramenta_service import ns as ns_ferramenta

api.init_app(blueprint)
app.register_blueprint(blueprint)

#REGISTRAR as rotas
api.add_namespace(ns_ferramenta)


log.info('>> LIVRARIA API http://{}'.format(app.config['SERVER_NAME']))
app.run(debug=True)