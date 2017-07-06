"""Starts the service and injects the dependencies.
"""


import lamarck

from configs import DB_EVOLUTIONS_PATH, DB_CREDENTIALS_SET
from models import Populator


if __name__ == '__main__':
    ddl_controller = lamarck.DDLController(DB_EVOLUTIONS_PATH, DB_CREDENTIALS_SET['master'])
    ddl_controller.evolve()

    Populator.populate(DB_CREDENTIALS_SET)
