"""Starts the service and injects the dependencies.
"""


if __name__ == '__main__':
    import lamarck
    import logging
    import time

    from configs import LOGGING, EXECUTION_DATETIME, DB_EVOLUTIONS_PATH, DB_CREDENTIALS_SET
    from models import Populator


    logging.Formatter.converter = time.gmtime
    logging.basicConfig(
        filename=LOGGING['filename'],
        level=LOGGING['level'],
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )

    logger = logging.getLogger(__name__)


    logger.info('Starting application.')

    ddl_controller = lamarck.DDLController(DB_EVOLUTIONS_PATH, DB_CREDENTIALS_SET['master'])
    ddl_controller.evolve()

    logger.info('Starting service.')

    Populator.populate(DB_CREDENTIALS_SET)
