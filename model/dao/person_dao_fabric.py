
from model.dao.person_dao import PersonDAO
from model.dao.member_dao import MemberDAO
from model.dao.coach_dao import CoachDAO


class PersonDAOFabric:

    def __init__(self, database_session):
        self._database_session = database_session

    def get_dao(self, type=None):
        if type is None:
            return PersonDAO(self._database_session)

        if type == 'member':
            return MemberDAO(self._database_session)
        elif type == 'coach':
            return CoachDAO(self._database_session)
        else:
            return PersonDAO(self._database_session)