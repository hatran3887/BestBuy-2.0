import pytest
from models.products import Product


def test_create_product():
    sut = Product('Macbook Pro', 1299, 5)
    assert sut.name == 'Macbook Pro'
    assert sut.price == 1299
    assert sut.quantity == 5


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product('', 1299, 5)
    with pytest.raises(ValueError):
        Product('Macbook Pro', '1299', 5)
    with pytest.raises(ValueError):
        Product('Macbook Pro', -1299, 5)
    with pytest.raises(ValueError):
        Product('Macbook Pro', 1299, '5')
    with pytest.raises(ValueError):
        Product('Macbook Pro', 1299, -1)


def test_product_becomes_inactive():
    sut = Product('Macbook Pro', 1299, 0)
    assert not sut.active
    sut = Product('Macbook Pro', 1299, 1)
    assert sut.active
    sut.set_quantity(0)
    assert not sut.active


def test_bye_modifies_quantity():
    sut = Product('Macbook Pro', 1299, 5)
    bought_product = sut.buy(4)
    assert sut.quantity == 1
    assert bought_product == 1299 * 4


def test_out_of_stock():
    sut = Product('Macbook Pro', 1299, 5)
    with pytest.raises(ValueError):
        sut.buy(6)