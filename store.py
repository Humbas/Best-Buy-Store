import products


class Store:
    def __init__(self, product_list):
        self.products = list(product_list)

    def add_product(self, product):
        self.products.append(product)
        return self.products

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of items in the store."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        """Returns a list of all active products."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list) -> float:
        """buys the product based on the shoppinglist """
        total_quantity = 0
        for product, quantity in shopping_list:
            total_quantity = product.buy(quantity)
        return total_quantity
