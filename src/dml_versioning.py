"""Responsible for keep data versioned.
"""


import psycopg2


def populate(ModelClass, credentials):
    session = psycopg2.connect(**credentials)

    for record in ModelClass.get_permitted_records():
        model = ModelClass(*record)
        if not model.exists(session):
            model.save(session)

    session.close()
