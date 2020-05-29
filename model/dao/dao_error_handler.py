import logging

from exceptions import ResourceNotFound, Error
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


def dao_error_handler(func):
    """
    Decorator pattern
    https://www.python.org/dev/peps/pep-0318/
    """
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoResultFound:
            logging.error("NoResultFound caught from SQLAlchemy")
            raise ResourceNotFound("Resource not found")
        except IntegrityError as e:
            logging.debug("Integrity error caught from SQLAlchemy (%s)" % str(e))
            raise Error("Error data may be malformed")
        except SQLAlchemyError as e:
            raise Error("An error occurred (%s)" % str(e))

    return handler
