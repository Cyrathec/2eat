import logging
import sys
from model.database import DatabaseEngine
from model.backet import Basket
from controller.order_controller import OrderController

def main():

    # configure logging
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    logging.info("Starting 2eat")

    # Init db
    logging.info("Init database")
    database_engine = DatabaseEngine(url='sqlite:///database.db')
    database_engine.create_database()


if __name__ == "__main__":
    main()
