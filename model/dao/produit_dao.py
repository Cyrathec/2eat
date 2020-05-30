from model.mapping.produit import Produit
from model.dao.dao import DAO
from model.dao.dao_error_handler import dao_error_handler


class ProduitDAO(DAO):
    """
    Sport Mapping DAO
    """

    @dao_error_handler
    def get(self, id):
        return self._database_session.query(Produit).filter_by(id=id).one()

    @dao_error_handler
    def get_all(self):
        return self._database_session.query(Produit).order_by(Produit.name).all()

    @dao_error_handler
    def get_by_name(self, name: str):
        return self._database_session.query(Produit).filter_by(name=name).one()

    @dao_error_handler
    def create(self, data: dict):
        produit = Produit(name=data.get('name'), description=data.get('description'))
        self._database_session.add(produit)
        self._database_session.flush()
        return produit

    @dao_error_handler
    def update(self, sport: Produit, data: dict):
        if 'name' in data:
            sport.name = data['name']
        if 'description' in data:
            sport.description = data['description']

        self._database_session.merge(sport)
        self._database_session.flush()

        return sport

    @dao_error_handler
    def delete(self, entity):
        self._database_session.delete(entity)
