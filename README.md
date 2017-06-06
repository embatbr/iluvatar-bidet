# Bidet

A generic bid-ask system. Bidet may be used in several scenarios, such as:

- Cryptocurrency exchange;
- Uber-like app paid with Bitcoin;
- Ebay-like app.

## Overview

The initial idea is to create an abstract system to arbitrate negotiations using the bid-ask concept. Important components may be:

- **Security** or **product** traded;
- Bids and asks (basically, **orders**) rankings:
    - Sorted by price:
        - Higher bids before lower bids;
        - Lower asks before higher asks.
    - Sorted by creation time:
        - When orders have same price;
        - Grouped by user.
- **Space** where order actuates:
    - Spaces are self-contained markets:
        - Can be static or dynamic;
        - Orders dispute preference of execution against others in the same space.
    - Can be different cryptocurrencies (BTC is one space, LTC is another and etc.);
    - Different products (for Ebay-like app);
    - Or different regions in the map (for the Uber-like app).

## Technologies/Architecture

What types of technologies may be needed:

- REST for public/user APIs:
    - Easy to work with;
    - Malleable.
- Thrift for internal communication between microservices:
    - Fast;
    - Exact;
    - Small.
- A performatic database that centralizes the orders (avoiding that 2 instances of the order handler microservice execute agains the same product):
    - PostgreSQL or Redis?
    - Orders must be read by the "arbitrator" after properly created and validated:
        - Sorts Redis structures by timestamp?
        - Do a Change Data Capture (CDC) from PostgreSQL xlog?
- Preferable to use one single programming language:
    - Python:
        - Easy to use;
        - Performance may be an issue.
    - JavaScript:
        - Fast, if using a proper framework (e.g., NodeJS);
        - Callback functions are a pain in the ass.
    - Java:
        - Lots of codes and good with concurrency;
        - Has Scala (the Java that works);
        - But it is Java.
    - C/C++:
        - May be the fastest one;
        - Gives me full freedom and control;
        - May fuck everything due to a simple mistypo.
