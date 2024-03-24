from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder(Pizza):
    def __init__(self, time):
        self.time = time
        self.pizza = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizza.append(pizza)

    def getOrderDescription(self):
        totalP = 0
        info = "******\n"
        info += "Order Time: {}\n".format(self.time)
        for i in self.pizza:
            info += i.getPizzaDetails()
            info += "\n"
            info += "----\n"
            totalP += i.getPrice()
        info += "TOTAL ORDER PRICE: ${:.2f}\n".format(totalP)
        info += "******\n"
        return info

