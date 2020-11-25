from .. import db, ma

class Aluguel(db.Model):
    __tablename__ = 'alugueis'

    id = db.Column(db.Integer,primary_key=True, server_default=db.FetchedValue())
    modelo = db.Column(db.String(120))
    tipo = db.Column(db.String(120))
    marca = db.Column(db.String(120))
    preco = db.Column(db.String(120))
    cliente = db.Column(db.String(120))
    telcli = db.Column(db.String(120))

class AluguelSchema(ma.Schema):
    class Meta:
        fields = ('id','modelo','tipo','marca', 'preco','cliente','telcli')