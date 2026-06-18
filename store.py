class Store:
    def __init__(self, products):
        self.products = products


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self):
        return sum([product.quantity for product in self.products])


    def get_all_products(self):
        return self.products


    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
