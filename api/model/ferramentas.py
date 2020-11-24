from .. import db, ma

class Ferramenta(db.Model):
    __tablename__ = "ferramentas"

    id = db.Column(db.Integer,primary_key=True, server_default=db.FetchedValue())
    modelo = db.Column(db.String(120))
    marca = db.Column(db.String(120))
    tipo = db.Column(db.String(120))
    preco = db.Column(db.String(120))
    quantidade = db.Column(db.String(10))

class FerramentaSchema(ma.Schema):
    class Meta:
        fields = ('id','modelo','marca','tipo','preco','quantidade')  