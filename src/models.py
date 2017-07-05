"""Entities representation, both high (trading) and low (database) level, as
well as trading logic.
"""


import decimal
import json
import psycopg2


class Model(object):

    def __init__(self, read_only=False):
        self.__read_only = read_only
        self.__json_repr = dict()
        self.__repr_str = ''

    def as_json(self):
        if not(self.__json_repr) or not(self.__read_only):
            classname = self.__class__.__name__
            class_attr = self.__class__.__dict__['_%s__json_keys' % (classname)]

            self.__repr_str = list()

            for key in class_attr:
                value = self.__dict__['_%s__%s' % (classname, key)]
                self.__json_repr[key] = value

                value = "'%s'" % value if isinstance(value, str) else value
                self.__repr_str.append("%s: %s" % (key, value))

            # good for logging
            self.__repr_str = "%s { %s }" % (classname, ", ".join(self.__repr_str))

        return self.__json_repr

    def __repr__(self):
        if not(self.__repr_str) or not(self.__read_only):
            self.as_json()
        return self.__repr_str

    def __validate(self, *args):
        return False

    def save(self, session, *args):
        self.__validate(args)

        sql_insert = self.__sql_insert__.format(self.__schema__, self.__table__)
        sql_insert = sql_insert % tuple(*args)

        cur = session.cursor()

        saved = False
        try:
            cur.execute(sql_insert)
            saved = True
            print('[INFO] object {} stored.'.format(self))

        except psycopg2.IntegrityError as e:
            msg = str(e).strip()

            if msg == 'duplicate key value violates unique constraint "{}_pkey"'.format('currencies'):
                print('[ERROR] object {} duplicated.'.format(self))
            else:
                print(msg)

        session.commit()

        cur.close()

        return saved

    @staticmethod
    def _get_permitted_records():
        return list()

    @staticmethod
    def _populate(model_sub_class, db_credentials):
        assert model_sub_class != Model, 'Class Model cannot populate a database.'

        session = psycopg2.connect(**db_credentials)

        for record in model_sub_class._get_permitted_records():
            model = model_sub_class(*record)
            model.save(session)

        session.close()


class Currency(Model):

    __schema__ = '_bidet_financial'
    __table__ = 'currencies'

    __sql_insert__ = "INSERT INTO {}.{} (symbol, canon_name, decimal_places) VALUES ('%s', '%s', %d)"

    __permitted_records = [
        ('btc', 'bitcoin', 8),
        ('ltc', 'litecoin', 8),
        ('eth', 'ethereum', 18)
    ]

    __json_keys = ['symbol', 'canon_name']

    def __init__(self, symbol, canon_name, decimal_places):
        super(Currency, self).__init__(read_only=True)

        records = self.__validate(symbol, canon_name, decimal_places)
        (self.__symbol, self.__canon_name, self.__decimal_places) = records

    symbol = property(lambda self: self.__symbol)
    canon_name = property(lambda self: self.__canon_name)
    decimal_places = property(lambda self: self.__decimal_places)

    def __validate(self, symbol, canon_name, decimal_places):
        assert isinstance(symbol, str), 'Symbol must be a string.'
        symbol = symbol.strip().lower()
        assert symbol != '', 'Symbol cannot be empty.'

        assert isinstance(canon_name, str), 'Canonical name must be a string.'
        canon_name = canon_name.strip().lower()
        assert canon_name != '', 'Canonical name cannot be empty.'

        assert isinstance(decimal_places, int) and decimal_places >= 0, \
            'Decimal places cannot be negative.'

        records = (symbol, canon_name, decimal_places)
        assert records in Currency.__permitted_records, 'Non-permitted record tuple.'

        return records

    def save(self, session):
        return super(Currency, self).save(session, [self.symbol, self.canon_name, self.decimal_places])

    @staticmethod
    def _get_permitted_records():
        return Currency.__permitted_records[:]

    @staticmethod
    def populate(db_credentials):
        Model._populate(Currency, db_credentials)


class Populator(object):

    __sql_grant_schema__ = "GRANT USAGE on SCHEMA {} TO {}"
    __sql_revoke_schema__ = "REVOKE USAGE on SCHEMA {} FROM {}"

    __sql_grant_table__ = "GRANT INSERT on TABLE {}.{} TO {}"
    __sql_revoke_table__ = "REVOKE INSERT on TABLE {}.{} FROM {}"

    __permitted_users = [
        'bidet_master',
        'bidet_populator'
    ]

    __model_sub_class_list = [Currency]

    @staticmethod
    def __validate(db_user):
        assert db_user in Populator.__permitted_users, "User '{}' not allowed.".format(db_user)

    @staticmethod
    def __grant_or_revoke(session, cur, db_user):
        for model_sub_class in Populator.__model_sub_class_list:
            cur.execute(Populator.__sql_grant_schema__.format(model_sub_class.__schema__,
                                                              db_user))

            cur.execute(Populator.__sql_grant_table__.format(model_sub_class.__schema__,
                                                             model_sub_class.__table__,
                                                             db_user))

        session.commit();

    @staticmethod
    def populate(db_credentials_set):
        Populator.__validate(db_credentials_set['master']['user'])
        Populator.__validate(db_credentials_set['populator']['user'])

        session = psycopg2.connect(**db_credentials_set['master'])
        cur = session.cursor()

        Populator.__grant_or_revoke(session, cur, db_credentials_set['populator']['user'])

        for model_sub_class in Populator.__model_sub_class_list:
            model_sub_class.populate(db_credentials_set['populator'])

        Populator.__grant_or_revoke(session, cur, db_credentials_set['populator']['user'])

        cur.close()
        session.close()

        # this credential's only purpose is to be used in this function, therefore its deletion here
        del db_credentials_set['populator']
