BEGIN;


CREATE SCHEMA _bidet_financial;

CREATE TABLE _bidet_financial.currencies (
    symbol VARCHAR(10) NOT NULL PRIMARY KEY,
    canon_name VARCHAR(20) NOT NULL UNIQUE,
    decimal_places INT NOT NULL DEFAULT 0,

    _saved_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);


-- CREATE SCHEMA _bidet_trading;


COMMIT;
