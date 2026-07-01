# Best Buy

A small command-line store program. It keeps an inventory of products and lets
you list them, see the total stock, and place an order from a simple menu.
Products can carry promotions, and the store supports regular, non-stocked and
per-order-limited products.

## Requirements

- Python 3.10+ (uses the `match` statement)
- No external dependencies to run the program
- `pytest` to run the tests (see `requirements.txt`)

## Usage

```bash
python main.py
```

You'll get a menu:

```
        Store Menu
        ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

When making an order, enter the product number and the amount you want. Leave
both fields empty to finish and see the total price.

## Product types

- **Product** — a normal product with name, price and stock quantity.
- **NonStockedProduct** — a product with no stock limit (e.g. a software
  license); its quantity is always 0 and shown as `Unlimited`.
- **LimitedProduct** — a product that can only be bought up to a maximum amount
  per order (e.g. shipping).

## Promotions

A product can have one promotion attached. Available promotions:

- **SecondHalfPrice** — every second item is half price.
- **ThirdOneFree** — every third item is free.
- **PercentDiscount** — a fixed percentage off the whole line.

## Project structure

- `main.py` — the interactive menu and program entry point.
- `models/products.py` — `Product` and its `NonStockedProduct` /
  `LimitedProduct` subclasses.
- `models/promotions.py` — the `Promotion` base class and the concrete
  promotions.
- `models/store.py` — `Store` class: holds products and handles orders
  (with stock rollback if an order line fails).
- `unit_tests/test_product.py` — pytest tests for the `Product` class.

## Running the tests

```bash
pytest
```
