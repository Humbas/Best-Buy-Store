class Product:

    def __init__(self, name, price, quantity):
        """constructors"""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = bool

        """methods"""

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
            if quantity > 0:
                self.quantity = self.quantity - quantity
                total_price = self.quantity * self.price
                return total_price
            else:
                print("Hey, you have to buy at least one!")
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
