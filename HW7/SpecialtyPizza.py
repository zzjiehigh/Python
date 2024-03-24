from Pizza import Pizza
from CustomPizza import CustomPizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        self.size = size
        self.name = name
        if self.size == "S":
            self.price = 12.00
        elif self.size == "M":
            self.price = 14.00
        else:
            self.price = 16.00
            
    def getPizzaDetails(self):
        info = "SPECIALTY PIZZA\nSize: {}\nName: {}\n".format(self.size, self.name)
        info += "Price: ${:.2f}\n".format(self.price)
        return info 

