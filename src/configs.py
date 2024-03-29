"""Global settings, used project wide. Also, contains variables for sensitive
information.
"""


import logging
import os
import pendulum as pdm


PROJECT_ROOT_PATH = os.environ.get('PROJECT_ROOT_PATH', '/')

EXECUTION_DATETIME = os.environ.get('EXECUTION_DATETIME', pdm.utcnow().strftime('%Y_%m_%d_%H_%M_%S'))

LOGGING = {
    'path': '{}/logs'.format(PROJECT_ROOT_PATH),
    'level': logging.DEBUG
}
# LOGGING['filename'] = '{}/app_{}.log'.format(LOGGING['path'], EXECUTION_DATETIME)
LOGGING['filename'] = '{}/app.log'.format(LOGGING['path'])

DB_PATH = '{}/db'.format(PROJECT_ROOT_PATH)
DB_EVOLUTIONS_PATH = '{}/evolutions'.format(DB_PATH)

DB_CREDENTIALS_SET = {
    'master': {
        'host': os.environ.get('DB_CREDENTIALS_MASTER_HOST', 'localhost'),
        'port': int(os.environ.get('DB_CREDENTIALS_MASTER_PORT', '5432')),
        'dbname': os.environ.get('DB_CREDENTIALS_MASTER_DBNAME', 'bidet'),
        'user': os.environ.get('DB_CREDENTIALS_MASTER_USER', 'bidet_master'),
        'password': os.environ.get('DB_CREDENTIALS_MASTER_PASSWORD', 'password')
    },
    'populator': {
        'host': os.environ.get('DB_CREDENTIALS_POPULATOR_HOST', 'localhost'),
        'port': int(os.environ.get('DB_CREDENTIALS_POPULATOR_PORT', '5432')),
        'dbname': os.environ.get('DB_CREDENTIALS_POPULATOR_DBNAME', 'bidet'),
        'user': os.environ.get('DB_CREDENTIALS_POPULATOR_USER', 'bidet_populator'),
        'password': os.environ.get('DB_CREDENTIALS_POPULATOR_PASSWORD', 'password')
    }
}
