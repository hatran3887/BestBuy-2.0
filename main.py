"""The main module, display the menu and handle users choices"""
from models import products as products_module, store, promotions


def pretty_print_product_list(products):
    """Print a numbered list of products."""
    print("------")
    for index, product in enumerate(products):
        print(index + 1, end=". ")
        product.show()
    print("------")


def order_a_products(products, product, amount):
    """Validate a single order line and return (product, amount) or None."""
    try:
        product = int(product)
        amount = int(amount)
    except ValueError:
        return None

    if product not in range(1, len(products) + 1):
        return None

    chosen_product = products[product - 1]
    return chosen_product, amount


def place_order(products):
    """Prompt the user for order lines and return the shopping cart."""
    pretty_print_product_list(products)
    print('When you want to finish order, enter empty text.')
    shopping_cart = []
    while True:
        product = input('Which product # do you want? ')
        amount = input('What amount do you want? ')
        if not product and not amount:
            return shopping_cart
        else:
            ordered_product = order_a_products(products, product, amount)
            if ordered_product:
                shopping_cart.append(ordered_product)
            else:
                print('Error adding product!')


def start(store):
    """Run the interactive store menu loop."""
    while True:
        print("""\n\tStore Menu
\t----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit""")
        user_choice = ""
        while user_choice not in ["1", "2", "3", "4"]:
            user_choice = input("Please choose a number: ")

        match int(user_choice):
            case 1:
                pretty_print_product_list(store.get_all_products())
            case 2:
                print(f"Total of {store.get_total_quantity()} items in store")
            case 3:
                order = place_order(store.get_all_products())
                if order:
                    try:
                        total = store.order(order)
                    except ValueError:
                        print('Error adding product!')
                    else:
                        print(f'********')
                        print(f'Order made! Total payments: ${total}')
            case 4:
                return


def main():
    """Program entry point."""
    # setup initial stock of inventory
    product_list = [products_module.Product("MacBook Air M2", price=1450, quantity=100),
                    products_module.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products_module.Product("Google Pixel 7", price=500, quantity=250),
                    products_module.NonStockedProduct("Windows License", price=125),
                    products_module.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()