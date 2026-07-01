"""Promotion module, handle all kinds of promotions"""
from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """Abstract method to apply the promotion"""
        pass


class SecondHalfPrice(Promotion):
    """Promotion class for half price promotion on second item"""

    def apply_promotion(self, product, quantity) -> float:
        """Return the price with second half price promotion"""
        half_price_count = quantity // 2
        full_price_count = quantity - half_price_count
        return product.price * full_price_count + product.price * half_price_count * 0.5


class ThirdOneFree(Promotion):
    """Promotion class for third one free promotion"""

    def apply_promotion(self, product, quantity) -> float:
        """Return the price with third one free promotion"""
        free_count = quantity // 3
        return product.price * (quantity - free_count)


class PercentDiscount(Promotion):
    """Promotion class for percent discount"""

    def __init__(self, name, percent):
        """Initialize the promotion class with percent discount"""
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """Return the percent discount promotion price"""
        return product.price * quantity * (100 - self.percent) / 100
