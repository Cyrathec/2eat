from model.mapping.member import Member
from model.dao.person_dao import PersonDAO
from model.dao.dao_error_handler import dao_error_handler


class MemberDAO(PersonDAO):
    """
    Member Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session, person_type=Member)

    @dao_error_handler
    def create(self, data: dict):
        member = Member(firstname=data.get('firstname'), lastname=data.get('lastname'), email=data.get('email'),
                        medical_certificate=data.get('medical_certificate', False))
        if 'address' in data.keys():
            address = data['address']
            member.set_address(address['street'], address['postal_code'], address['city'],
                               address.get('country', 'FRANCE'))
        self._database_session.add(member)
        self._database_session.flush()
        return member

    @dao_error_handler
    def update(self, member: Member, data: dict):
        # Update Person data
        super().update(member, data)

        # Update Member data
        if 'medical_certificate' in data:
            member.medical_certificate = data['medical_certificate']

        self._database_session.merge(member)
        self._database_session.flush()

        return member
