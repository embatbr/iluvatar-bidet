"""Global settings, used project wide. Also, contains variables for sensitive
information.
"""


import os


PROJECT_ROOT_PATH = os.environ.get('PROJECT_ROOT_PATH', '/')

DB_PATH = '{}/db'.format(PROJECT_ROOT_PATH)
DB_EVOLUTIONS_PATH = '{}/evolutions'.format(DB_PATH)

DB_CREDENTIALS_MASTER = {
    'host': os.environ.get('DB_CREDENTIALS_HOST', 'localhost'),
    'port': int(os.environ.get('DB_CREDENTIALS_PORT', '5432')),
    'dbname': os.environ.get('DB_CREDENTIALS_DBNAME', 'bidet'),
    'user': os.environ.get('DB_CREDENTIALS_USER', 'bidet_master'),
    'password': os.environ.get('DB_CREDENTIALS_PASSWORD', 'password')
}
