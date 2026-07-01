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
        self.promotion = None

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
        print(f'{self.name}, Price: ${self.price}, Quantity: {self.quantity}, '
              f'Promotion: {self.get_promotion_name()}')

    def buy(self, quantity):
        """Buy the given quantity, reduce stock and return the total price."""
        if type(quantity) != int or quantity <= 0:
            raise ValueError("Product quantity is required")
        if quantity > self.quantity:
            raise ValueError("Out of stock")
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return self.get_total_price(quantity)

    def set_promotion(self, promotion):
        """Set the promotion"""
        self.promotion = promotion

    def get_promotion(self):
        """Return the current promotion."""
        return self.promotion

    def get_promotion_name(self):
        """Return the name of the promotion and None if not available."""
        promotion = self.promotion.name if self.promotion else "None"
        return promotion

    def get_total_price(self, quantity):
        """Return the total price of the product."""
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return quantity * self.price


class NonStockedProduct(Product):
    """A non-stocked product with quantity 0."""

    def __init__(self, name, price):
        """Create a non-stocked product."""
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        """Ignore because the quantity is always 0."""
        pass

    def buy(self, quantity):
        """Buy the given quantity and return the total price."""
        if type(quantity) != int or quantity <= 0:
            raise ValueError("Product quantity is required")
        return self.get_total_price(quantity)

    def show(self):
        """Print a one-line summary of the product."""
        print(f'{self.name}, Price: ${self.price}, Quantity: Unlimited, '
              f'Promotion: {self.get_promotion_name()}')


class LimitedProduct(Product):
    """A product, which is limited per order"""

    def __init__(self, name, price, quantity, maximum):
        """Create a limited product."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """Print a one-line summary of the product."""
        print(f'{self.name}, Price: ${self.price}, Quantity: {self.quantity}, '
              f'Maximum: {self.maximum}, Promotion: {self.get_promotion_name()}')

    def buy(self, quantity):
        """Buy the given quantity and return the total price."""
        if type(quantity) != int or quantity <= 0 or quantity > self.maximum:
            raise ValueError("Product quantity should be an int greater than 0 and less than or equal the maximum")
        return self.get_total_price(quantity)
