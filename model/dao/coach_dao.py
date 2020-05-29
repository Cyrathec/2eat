from model.mapping.coach import Coach
from model.dao.person_dao import PersonDAO
from model.dao.dao_error_handler import dao_error_handler


class CoachDAO(PersonDAO):
    """
    Coach Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session, person_type=Coach)

    @dao_error_handler
    def create(self, data: dict):
        coach = Coach(firstname=data.get('firstname'), lastname=data.get('lastname'), email=data.get('email'),
                      contract=data.get('contract'), degree=data.get('degree'))
        if {'street', 'city', 'postal_code'} < set(data.keys()):
            coach.set_address(data['street'], data['postal_code'], data['city'], data.get('country', 'FRANCE'))
        self._database_session.add(coach)
        self._database_session.flush()
        return coach

    @dao_error_handler
    def update(self, coach: Coach, data: dict):
        # Update Person data
        super().update(coach, data)
        if 'contract' in data:
            coach.contract = data['contract']
        if 'degree' in data:
            coach.degree = data['degree']

        self._database_session.merge(coach)
        self._database_session.flush()
        return coach
