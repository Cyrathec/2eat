import re
import logging

from model.dao.person_dao_fabric import PersonDAOFabric
from model.dao.product_dao import ProductDAO

from exceptions import Error, InvalidData


class PersonController:
    """
    Member actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_people(self, person_type=None):
        logging.info("Get restaurant ")
        with self._database_engine.new_session() as session:
            dao = PersonDAOFabric(session).get_dao()
            members = dao.get_all()
            members_data = [member.to_dict() for member in members]
        return members_data

    def get_restaurant(self, restaurant_id, restaurant_type=None):
        logging.info("Get restaurant %s" % restaurant_id)
        with self._database_engine.new_session() as session:
            dao = PersonDAOFabric(session).get_dao(type=restaurant_type)
            member = dao.get(restaurant_id)
            member_data = member.to_dict()
        return member_data

    def get_member(self, member_id):
        return self.get_restaurant(member_id, )

    def create_person(self, data, person_type=None):
        logging.info("Create member with data %s" % str(data))
        self._check_person_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                dao = PersonDAOFabric(session).get_dao(type=person_type)
                member = dao.create(data)
                member_data = member.to_dict()
                return member_data
        except Error as e:
            # log error
            logging.error("An Error occured (%s)" % str(e))
            raise e

    def create_member(self, data):
        return self.create_person(data, 'member')

    def create_coach(self, data):
        return self.create_person(data, 'coach')

    def _update_person(self, member_id, member_data, person_type=None):
        logging.info("Update %s with data: %s" % (member_id, str(member_data)))
        with self._database_engine.new_session() as session:
            dao = PersonDAOFabric(session).get_dao(type=person_type)
            person = dao.get(member_id)

            person = dao.update(person, member_data)
            return person.to_dict()

    def update_person(self, member_id, member_data):
        self._check_person_data(member_data, update=True)
        return self._update_person(member_id, member_data, person_type='person')

    def update_member(self, member_id, data):
        self._check_member_data(data, update=True)
        return self._update_person(member_id, data, person_type='member')

    def update_coach(self, member_id, data):
        self._check_coach_data(data, update=True)
        return self._update_person(member_id, data, person_type='coach')

    def add_sport_person(self, person_id, sport_id, level):
        logging.info("Add sport %s to person %s" % (sport_id, person_id))
        with self._database_engine.new_session() as session:
            dao = PersonDAOFabric(session).get_dao()
            person = dao.get(person_id)
            sport = ProductDAO(session).get(sport_id)
            person.add_sport(sport, level, session)
            return person.to_dict()

    def delete_sport_person(self, person_id, sport_id):
        logging.info("Delete sport %s from user %s" % (person_id, sport_id))
        with self._database_engine.new_session() as session:
            dao = PersonDAOFabric(session).get_dao()
            person = dao.get(person_id)
            sport = ProductDAO(session).get(sport_id)
            person.delete_sport(sport, session)
            return person.to_dict()

    def delete_person(self, member_id, person_type=None):
        logging.info("Delete person %s" % member_id)
        with self._database_engine.new_session() as session:
            dao = PersonDAOFabric(session).get_dao(type=person_type)
            member = dao.get(member_id)
            dao.delete(member)

    def search_restaurant(self, restaurant_name, person_type=None):
        logging.info("Search restaurant %s" % (restaurant_name))
        # Query database
        with self._database_engine.new_session() as session:
            dao = PersonDAOFabric(session).get_dao(type=person_type)
            member = dao.get_by_name(restaurant_name)
            return member.to_dict()

    def _check_member_data(self, data, update=False):
        self._check_person_data(data, update=update)
        specs = {
            'medical_certificate': {"type": bool},
        }
        self._check_data(data, specs, update=update)

    def _check_coach_data(self, data, update=False):
        self._check_person_data(data, update=update)
        specs = {
            'degree': {"type": str},
            'certificate': {"type": str}
        }
        self._check_data(data, specs, update=update)

    def _check_person_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        specs = {
            'restaurant_name': {"type": str, "regex": name_pattern}  
        }
        self._check_data(data, specs, update=update)

        if 'address' in data:
            address = data['address']
            specs = {
                'street': {"type": str},
                'postal_code': {"type": int},
                'city': {"type": str}
            }
            self._check_data(address, specs, update=update)

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