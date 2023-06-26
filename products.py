import math


class Product:

    def __init__(self, name, price, quantity):
        """its necessary to check if all fields are properly set"""
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price should higher than zero")
        if quantity < 0:
            raise ValueError("Quantity should higher than zero")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = bool
        self.promotion = None

        """methods"""

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_quantity(self):
        """returns the quantity variable in float """
        return float(self.quantity)

    def set_quantity(self, quantity) -> float:
        self.quantity = int(quantity)
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """id the product texist or is set to active"""
        if self.quantity > 0 and self.active:
            return True
        else:
            return False

    def activate(self):
        """activates the product."""
        self.active = True
        return self.active

    def deactivate(self):
        """Deactivates the product."""
        self.active = False
        return self.active

    def show(self) -> str:
        print(str(self.name) + ", Price: " + str(self.price) + ", Quantity:" + str(self.quantity))

    def buy(self, quantity) -> float:
        total_price = 0
        if quantity <= 0:
            print("Quantity to buy must be greater than zero.")

        elif not self.active:
            print("Cannot buy an inactive product.")

        elif quantity > self.quantity:
            print("Not enough quantity available.")

        elif self.promotion:
            total_price = self.promotion.add_promotion(self, quantity)
        else:
            total_price = self.price * quantity
            # subtract quantity from storage
        self.quantity -= quantity
        return total_price

    # this is one of my own functions
    def show_product(self):
        promotion_information = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f'{self.name}, Price: ${self.price}, Quantity: {self.quantity}, {promotion_information}'

    # this one is for my own use in the order section
    def product_dict(self) -> dict:
        product = {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'promotion': self.promotion
        }
        return product

    # this is one of my own functions
    def show_product_name(self) -> str:
        return self.name


# subclasses

# for non stocked products
class Non_Stocked(Product):
    """no need to keep quantity track"""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    # re-articulating show() method
    def show_product(self):
        """if quantity is zero, lets say its unlimited"""
        if self.quantity == 0:
            """set it unlimited"""
            return f'{self.name}, Price {self.price}, Quantity: Its unlimited!'
        else:
            return super().show()
        """else return normal show method from superclass"""


# for limited products

class Limited(Product):
    """takes main arguments from parent class and add maximum for maximum orders"""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    # new methods

    def show(self):
        return f'{self.name}, Price: {self.price}, Limited to {self.maximum} per order'

    def buy(self, quantity):
        if quantity > self.maximum:
            print("Quantity exceeds the maximum limit for this product.")

        elif quantity > self.quantity:
            print("Not enough quantity available.")
        else:
            self.quantity -= quantity
            total_price = self.price * quantity
            return total_price
