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
        """calculate discount for second item which is half price """
        if quantity >= 2:
            full_price_qt = quantity // 2
            """floor division by 2"""
            half_price_qt = quantity - full_price_qt
            """it simply means that quantity to be charged in half price corresponds to the subtraction of the total quantity 
             by its half """
            discounted_price = (full_price_qt * product.price) + (half_price_qt * product.price // 2)
        else:
            discounted_price = quantity * product.price

        return discounted_price


class ThirdFree(Promotion):
    def __init__(self, name):
        self.name = name

    def add_promotion(self, product, quantity):
        if quantity >= 3 and quantity % 3 == 0:
            full_price = product.price * quantity
            third = full_price // 3
            discounted_price = full_price - third
        else:
            discounted_price = quantity * product.price

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
