"""thus is for my own testing"""
import products
import promotions

"""start promotion"""
third_one_free = promotions.ThirdFree("Third One Free!")
second_half_price = promotions.SecondHalfPrice("Second Half price!")
forty_percent = promotions.Percentage("40% off!", percent=40)
Dumbbells = products.Product("Dumbbells 50kg", price=550, quantity=100)

"""buy Dumbells"""
Dumbbells.set_promotion(second_half_price)

""""set stocks"""

smith = products.Limited("Smith machine", price=1450, quantity=2, maximum=2)
strappers = products.Non_Stocked("strappers", price=50)
print(isinstance(strappers, products.Non_Stocked))
buy = smith.buy(2)
print(buy)
