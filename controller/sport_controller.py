import re
import logging

from model.dao.sport_dao import SportDAO

from exceptions import Error, InvalidData


class SportController:
    """
    Sport actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_sports(self):
        logging.info("List sports")
        with self._database_engine.new_session() as session:
            sports = SportDAO(session).get_all()
            sports_data = [sport.to_dict() for sport in sports]
        return sports_data

    def get_sport(self, sport_id):
        logging.info("Get sport %s" % sport_id)
        with self._database_engine.new_session() as session:
            sport = SportDAO(session).get(sport_id)
            sport_data = sport.to_dict()
        return sport_data

    def create_sport(self, data):
        logging.info("Create sport with data %s" % str(data))
        self._check_sport_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                dao = SportDAO(session)
                sport = dao.create(data)
                sport_data = sport.to_dict()
                return sport_data
        except Error as e:
            # log error
            logging.error("An Error occured (%s)" % str(e))
            raise e

    def update_sport(self, sport_id, sport_data):
        logging.info("Update sport %s with data: %s" % (sport_id, str(sport_data)))
        with self._database_engine.new_session() as session:
            dao = SportDAO(session)
            sport = dao.get(sport_id)
            sport = dao.update(sport, sport_data)
            return sport.to_dict()

    def delete_sport(self, sport_id):
        logging.info("Delete person %s" % sport_id)
        with self._database_engine.new_session() as session:
            dao = SportDAO(session)
            sport = dao.get(sport_id)
            dao.delete(sport)

    def search_sport(self, name):
        logging.info("Search sport %s" % name)
        # Query database
        with self._database_engine.new_session() as session:
            dao = SportDAO(session)
            sport = dao.get_by_name(name)
            return sport.to_dict()

    def _check_sport_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        specs = {
            "name": {"type": str, "regex": name_pattern},
            "description": {"type": str}
        }
        self._check_data(data, specs, update=update)

    def _check_data(self, data, specs, update=False):
        for mandatory, specs in specs.items():
            if not update:
                if mandatory not in data or data[mandatory] is None:
                    raise InvalidData("Missing value %s" % mandatory)
            else:
                if mandatory not in data:
                    continue
            value = data[mandatory]
            if "type" in specs and not isinstance(value, specs["type"]):
                raise InvalidData("Invalid type %s" % mandatory)
            if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
                raise InvalidData("Invalid value %s" % mandatory)