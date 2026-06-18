# Best Buy

A small command-line store program. It keeps an inventory of products and lets
you list them, see the total stock, and place an order from a simple menu.

## Requirements

- Python 3.10+ (uses the `match` statement)
- No external dependencies

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

## Project structure

- `products.py` — `Product` class: a single product with name, price and quantity.
- `store.py` — `Store` class: holds products and handles orders.
- `main.py` — the interactive menu and program entry point.
