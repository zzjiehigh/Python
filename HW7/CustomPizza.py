from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        self.size = size
        self.topping = []
        self.topNum = 0
        if self.size == "S":
            self.price = 8.00
        elif self.size == "M":
            self.price = 10.00
        else:
            self.price = 12.00

    def addTopping(self, topping):
        if self.size == "S":
            self.price += 0.5
        elif self.size == "M":
            self.price += 0.75
        else:
            self.price += 1.00
        self.topping.append(topping)

    def getPizzaDetails(self):
        info = "CUSTOM PIZZA\nSize: {}\nToppings:\n".format(self.size)
        for i in self.topping:
            info += "\t+ {}\n".format(i)
        info += "Price: ${:.2f}\n".format(self.price)
        return info 

