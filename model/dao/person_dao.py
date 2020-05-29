from model.mapping.person import Person
from model.dao.dao import DAO
from model.dao.dao_error_handler import dao_error_handler


class PersonDAO(DAO):
    """
    Person Mapping DAO
    """

    def __init__(self, database_session, person_type=Person):
        super().__init__(database_session)
        self._person_type = person_type

    @dao_error_handler
    def get(self, id):
        return self._database_session.query(self._person_type).filter_by(id=id).one()

    @dao_error_handler
    def get_all(self):
        return self._database_session.query(self._person_type).order_by(self._person_type.firstname).all()

    @dao_error_handler
    def get_by_name(self, firstname: str, lastname: str):
        return self._database_session.query(self._person_type)\
            .filter_by(firstname=firstname, lastname=lastname).one()

    @dao_error_handler
    def _update_address(self, member, address_data):
        if member.address is not None:
            if 'street' in address_data:
                member.address.street = address_data['street']
            if 'postal_code' in address_data:
                member.address.postal_code = address_data['postal_code']
            if 'city' in address_data:
                member.address.city = address_data['city']
            if 'country' in address_data:
                member.address.country = address_data['country']
        else:
            member.set_address(address_data['street'], address_data['postal_code'], address_data['city'],
                               address_data.get('country', 'FRANCE'))

    @dao_error_handler
    def update(self, member: Person, data: dict):
        if 'firstname' in data:
            member.firstname = data['firstname']
        if 'lastname' in data:
            member.lastname = data['lastname']
        if 'email' in data:
            member.email = data['email']
        if 'address' in data:
            self._update_address(member, data['address'])

        self._database_session.merge(member)
        self._database_session.flush()
        return member

    @dao_error_handler
    def delete(self, entity):
        self._database_session.delete(entity)
