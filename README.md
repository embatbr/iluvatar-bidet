# Bidet

<p align="center">
    <img src="logo.jpg" />
</p>

Version: 0.2.1

*Bidet* is the trading core. The microservice's instances receive requests only from a trading front-end named *Nasdaq*. In order to have several self-contained instances dealing with the same resource, the transaction lock is provided by database access (the transaction executes a sequence of linked operations in the database).

## Map

The project's root is composed of the following high level directories:

- [src](./src) - Python source code, containing packages and modules;
- [docs](./docs) - More detailed documentation than found in this document;
- [db](./db) - Database related material: configuration files, evolutions and etc.

## TODO

1. Document the database users with its details:
    - Permissions;
    - Number of simultaneous connections;
    - How to create it and which commands run before its use.
2. Use a proper logging strategy:
    - [Paddy](https://github.com/embatbr/paddy)
    - Links:
        - https://logmatic.io/blog/python-logging-with-json-steroids/
3. Write a test suite:
    1. Unit tests;
    2. System tests (initially a few to test the flow);
    3. Load tests;
    4. Stress tests.
4. Write the code to make trading:
    1. Order creation;
    2. Order activation (actual trading):
        - Isolated;
        - Atomic;
        - Consistent:
            - Maybe using a logic similar to blockchain;
            - An order must be linked to a previous order (executed or not?).
5. Create a CDC strategy:
    - Useful to maintain the trading order activation correctly ordered.
