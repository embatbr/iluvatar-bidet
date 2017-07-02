# Bidet

<p align="center">
    <img src="logo.jpg" />
</p>

Version: 0.1.1

*Bidet* is the trading core. The microservice's instances receive requests only from a trading front-end named *Nasdaq*. In order to have several self-contained instances dealing with the same resource, the transaction lock is provided by database access (the transaction executes a sequence of linked operations in the database).
