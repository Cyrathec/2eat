
class DAO:
    """
    DAO Interface Object
    """

    def __init__(self, database_session):
        self._database_session = database_session

    def get(self, id):
        raise NotImplementedError()

    def get_all(self):
        raise NotImplementedError()

    def create(self, data: dict):
        raise NotImplementedError()

    def update(self, entity, data: dict):
        raise NotImplementedError()

    def delete(self, entity):
        raise NotImplementedError()
