"""Starts the service and injects the dependencies.
"""


from lamarck import Lamarck

from configs import DB_EVOLUTIONS_PATH, DB_CREDENTIALS_MASTER
from models import Currency


if __name__ == '__main__':
    from configs import DB_CREDENTIALS_MASTER


    lamarck = Lamarck(DB_EVOLUTIONS_PATH, DB_CREDENTIALS_MASTER)
    lamarck.evolve_ddl()

    Currency.populate(DB_CREDENTIALS_MASTER)
