
from model.dao.person_dao import PersonDAO





class PersonDAOFabric:

    def __init__(self, database_session):
        self._database_session = database_session

    def get_dao(self):
        
        return PersonDAO(self._database_session)

        