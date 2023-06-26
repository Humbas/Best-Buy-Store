import pytest
from products import Product


def test_product():
    """ This will test if it returns an existing product with the expected parameters"""
    assert Product("Barbells 20kg", price=20, quantity=50)

    "a product should be deactivated in its quantity reaches zero"""
    barbell_press = Product("Incline Barbell press", price=740, quantity=1)

    "testing if is active, should be inactive if quantity is zero"""
    assert barbell_press.is_active() is True
    """ setting to zero and test activess"""

    barbell_press.set_quantity(0)
    assert barbell_press.is_active() is False

    "testing modifications on quantity"""
    barbell_press.set_quantity(1)
    barbell_press.buy(1)
    assert barbell_press.get_quantity() == 0

    """ using pytest method raises ValueError when error messages are found,
       that error messages should match the ones in the product constructor algorythm"""

    """testing large quantities"""
    barbell_press.get_quantity() == 100
    assert barbell_press.buy(200) > barbell_press.get_quantity()

    with pytest.raises(ValueError, match="Name cannot be empty"):
        Product("", price=50, quantity=10)

    with pytest.raises(ValueError, match="Price should higher than zero"):
        Product("Barbells 20kg", price=-1, quantity=100)

    with pytest.raises(ValueError, match="Quantity should higher than zero"):
        Product("Barbells 20kg", price=1, quantity=-1)


test_product()
