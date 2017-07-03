# Bidet

<p align="center">
    <img src="logo.jpg" />
</p>

Version: 0.2.0

*Bidet* is the trading core. The microservice's instances receive requests only from a trading front-end named *Nasdaq*. In order to have several self-contained instances dealing with the same resource, the transaction lock is provided by database access (the transaction executes a sequence of linked operations in the database).

## TODO

- Use a proper logging strategy;
- Write a test suite:
    - Unit tests;
    - System tests (initially a few to test the flow);
    - Load tests;
    - Stress tests.
- Write the code to make trading:
    - Order creation;
    - Order activation (actual trading):
        - Isolated;
        - Atomic;
        - Consistent:
            - Maybe using a logic similar to blockchain;
            - An order must be linked to a previous order (executed or not?).
- Create a CDC strategy:
    - Useful to maintain the trading order activation correctly ordered.
