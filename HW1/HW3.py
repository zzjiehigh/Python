from Animal import Animal
class Snake(Animal):
    def __init__(self, age = None, weight = None, venomAmount = None):
        super().__init__(venomAmount)
        self.venomAmount = venomAmount
    def getInfo(self):
        list_str = ""
        for i in self.venomAmount:
            list_str += "{}/".format(i)
        list_str = list_str[:-1]
        return "Snake, " + super().getInfo() + "Venom: {} mg".format(list_str)
        


