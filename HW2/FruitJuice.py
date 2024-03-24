from Beverage import Beverage
class FruitJuice(Beverage):
    def __init__(self, ounces = None, price = None, fruits = None):
        super().__init__(ounces, price)
        self.fruits = fruits

    def getInfo(self):
        list_str = ""
        for i in self.fruits:
            list_str += "{}/".format(i)
        list_str = list_str[:-1]
        return "{} Juice, ".format(list_str) + super().getInfo()        

