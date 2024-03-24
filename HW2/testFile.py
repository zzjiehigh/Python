import pytest
# imports the biggestInt function from lecture.py
from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from Coffee import Coffee
from DrinkOrder import DrinkOrder

def Beverage():
    assert Beverage(16, 20.5).getInfo() == "16 oz, $20.50"

def Coffee():
    assert Coffee(8, 3.0, "Espresso").getInfo() == "Espresso Coffee, 8 oz, $3.00"

def FruitJuice():
    assert FruitJuice(16, 4.5, ["Apple", "Guava"]).getInfo() == "Apple/Guava Juice, 16 oz, $4.50"

def DrinkOrder():
    assert c1 == Coffee(8, 3.0, "Espresso")
    assert juice == FruitJuice(16, 4.5, ["Apple", "Guava"])
    assert order == DrinkOrder()
    assert order.addBeverage(c1)
    assert order.addBeverage(juice)
    assert order.getTotalOrder() == "Order Items:/n* Espresso Coffee, 8 oz, $3.00/n* Apple/Guava Juice, 16 oz, $4.50/nTotal Price: $7.50"
