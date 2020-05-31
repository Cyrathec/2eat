import logging
import sys
from model.database import DatabaseEngine
from controller.person_controller import PersonController
from controller.sport_controller import SportController

from vue.root_frame import RootFrame

def main():

    # configure logging
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    logging.info("Start 2eat App")

    # Init db
    logging.info("Init database")
    database_engine = DatabaseEngine(url='sqlite:///database.db')
    database_engine.create_database()

    # controller
    person_controller = PersonController(database_engine)
    sport_controller = SportController(database_engine)

    # init vue
    root = RootFrame(person_controller, sport_controller)
    root.master.title("2eat app")
    root.show_menu()

    # start
    root.mainloop()


if __name__ == "__main__":
    main()
