"""Starts the service and injects the dependencies.
"""


from lamarck import Lamarck

from configs import DB_EVOLUTIONS_PATH, DB_CREDENTIALS_SET
from models import Populator


if __name__ == '__main__':
    lamarck = Lamarck(DB_EVOLUTIONS_PATH, DB_CREDENTIALS_SET['master'])
    lamarck.evolve_ddl()

    Populator.populate(DB_CREDENTIALS_SET)
