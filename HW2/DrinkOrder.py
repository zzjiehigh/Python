from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
class DrinkOrder():
    def __init__(self):
        self.drinks = []
    def addBeverage(self, beverage):
        self.drink = self.drinks.append(beverage)
    def getTotalOrder(self):
        item = "Order Items:\n"
        for i in self.drinks:
            item += "* " + i.getInfo() + "\n"
        total_p = 0
        for i in self.drinks:
            total_p += i.price
        return item + "Total Price: ${:.2f}".format(total_p)

