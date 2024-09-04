from Task04.Quantity import Quantity
from Task04.Price import Price


class Product:

    price = Price()
    quantity = Quantity()

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

