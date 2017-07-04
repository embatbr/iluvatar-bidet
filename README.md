# Bidet

<p align="center">
    <img src="logo.jpg" />
</p>

Version: 0.2.0

*Bidet* is the trading core. The microservice's instances receive requests only from a trading front-end named *Nasdaq*. In order to have several self-contained instances dealing with the same resource, the transaction lock is provided by database access (the transaction executes a sequence of linked operations in the database).

## TODO

1. Use a proper logging strategy;
2. Write a test suite:
    1. Unit tests;
    2. System tests (initially a few to test the flow);
    3. Load tests;
    4. Stress tests.
3. Write the code to make trading:
    1. Order creation;
    2. Order activation (actual trading):
        - Isolated;
        - Atomic;
        - Consistent:
            - Maybe using a logic similar to blockchain;
            - An order must be linked to a previous order (executed or not?).
4. Create a CDC strategy:
    - Useful to maintain the trading order activation correctly ordered.
