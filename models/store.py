class Store:
    """A store that holds a collection of products and handles orders."""

    def __init__(self, products):
        """Create a store from a list of Product objects."""
        self.products = products


    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)


    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)


    def get_total_quantity(self):
        """Return the total quantity of all products in the store."""
        return sum([product.quantity for product in self.products])


    def get_all_products(self):
        """Return the list of all products in the store."""
        return self.products


    def order(self, shopping_list):
        """Buy each (product, quantity) pair and return the total price."""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
