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
        try:
            if quantity < 0:
                raise ValueError(" Quantity should be higher than zero")
            if quantity > self.quantity:
                raise ValueError("Not enough quantity!")
            else:
                self.quantity = self.quantity - quantity
                total_price = self.quantity * self.price
                return total_price

        except TypeError:
            print("Please insert a number!")

    # this is one of my own functions
    def show_product(self):
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}'

    # this one is for my own use in the order section
    def product_dict(self) -> dict:
        product = {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
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
        super().__init__(name, price, quantity = 0)


    # re-articulating show() method
    def show(self):
        """if quantity is zero, lets say its unlimited"""
        if self.quantity == 0:
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
        return f'{self.name}, Price {self.price},  Limit per order: {self.maximum}'

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError("Maximum amount per order of this product exceeded")

        if quantity > self.quantity:
            raise ValueError("There is not enough quantity available")

        self.quantity = self.quantity - quantity
        total_price = self.quantity * self.price
        return total_price






