class Product:
    """A single product in the store, with a name, price and stock quantity."""

    def __init__(self, name, price, quantity):
        """Create a product, validating that the inputs are sensible."""
        if type(name) != str or not name:
            raise ValueError("Product name is required")
        if type(price) not in (float, int) or price < 0:
            raise ValueError("Product price is required")
        if type(quantity) != int or quantity < 0:
            raise ValueError("Product quantity is required")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0


    def get_quantity(self):
        """Return the current stock quantity."""
        return self.quantity


    def set_quantity(self, quantity):
        """Set the stock quantity, deactivating the product when it hits zero."""
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False
        elif self.quantity > 0:
            self.active = True


    def is_active(self):
        """Return whether the product is active."""
        return self.active


    def activate(self):
        """Mark the product as active."""
        self.active = True


    def deactivate(self):
        """Mark the product as inactive."""
        self.active = False


    def show(self):
        """Print a one-line summary of the product."""
        print(f'{self.name}, Price: ${self.price}, Quantity: {self.quantity}')


    def buy(self, quantity):
        """Buy the given quantity, reduce stock and return the total price."""
        if type(quantity) != int or quantity <= 0:
            raise ValueError("Product quantity is required")
        if quantity > self.quantity:
            raise ValueError("Out of stock")
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return quantity * self.price
