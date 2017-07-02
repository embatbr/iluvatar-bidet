"""Entities representation, both high (trading) and low (database) level, as
well as trading logic.
"""


import decimal


class Currency(object):

    __schema__ = '_bidet_financial'
    __table__ = 'currencies'

    __sql_insert__ = "INSERT INTO {}.{} (symbol, canon_name, decimal_places) VALUES ('%s', '%s', %d)"
    __sql_exists__ = "SELECT EXISTS (SELECT * FROM {}.{} WHERE symbol = '%s')"

    __permitted_records = [
        ('btc', 'bitcoin', 8),
        ('ltc', 'litecoin', 8),
        ('eth', 'ethereum', 18)
    ]

    def __init__(self, symbol, canon_name, decimal_places):
        records = self.__validate(symbol, canon_name, decimal_places)
        (self._symbol, self._canon_name, self._decimal_places) = records

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

    # TODO extract to superclass Model
    def save(self, session):
        self.__validate(self._symbol, self._canon_name, self._decimal_places)

        sql_insert = Currency.__sql_insert__.format(Currency.__schema__, Currency.__table__)
        sql_insert = sql_insert % (self._symbol, self._canon_name, self._decimal_places)

        cur = session.cursor()

        cur.execute(sql_insert)
        session.commit()

        cur.close()

    # TODO extract to superclass Model
    def exists(self, session):
        self.__validate(self._symbol, self._canon_name, self._decimal_places)

        sql_exists = Currency.__sql_exists__.format(Currency.__schema__, Currency.__table__)
        sql_exists = sql_exists % self._symbol

        cur = session.cursor()

        cur.execute(sql_exists)
        exists = cur.fetchone()[0]

        cur.close()

        return exists

    @staticmethod
    def get_permitted_records():
        return Currency.__permitted_records[:]
