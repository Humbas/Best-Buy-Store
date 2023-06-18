from abc import ABC, abstractmethod


class Promotion(ABC):
    name = "Promotion!!"

    # general method
    @abstractmethod
    def add_promotion(self, product, quantity):
        """returns discounted value"""
        pass


# subclasses

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        self.name = name

    def add_promotion(self, product, quantity):
        """calculate discount for second item which is half peice """
        if quantity >= 2:
            full_price_qt = quantity // 2
            """floor division by 2"""
            half_price_qt = quantity - full_price_qt
            """it simply means that quantity corresponds to the subtraction of the total quantity 
             by its half """
            discounted_price = (full_price_qt * product.price) + (half_price_qt * product.price)
        else:
            discounted_price = quantity * product.price

        return discounted_price


class ThirdFree(Promotion):
    def __init__(self, name):
        self.name = name

    def add_promotion(self, product, quantity):
        full_price_qt = quantity // 3
        """floor division by 3"""
        discounted_price = full_price_qt * product.price

        return discounted_price


class Percentage(Promotion):
    """Represents the discount indicated in the percent."""

    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def add_promotion(self, product, quantity):
        discount = self.percent / 100.0
        discounted_price = product.price * quantity * (1 - discount)

        return discounted_price
