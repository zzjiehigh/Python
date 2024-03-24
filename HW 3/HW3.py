class Animal:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight
        
    def setAge(self, age):
        self.age = age
        
    def setWeight(self, weight):
        self.weight = weight
    
    def getAge(self):
        return self.age
    
    def getWeight(self):
        return self.weight
    
    def getInfo(self):
        return "Age: {} years, Weight: {} lbs" \
               .format(self.age, self.weight)
    
class Snake(Animal):
    def __init__(self, age = None, weight = None, venomAmount = None):
        super().__init__(age, weight)
        self.venomAmount = venomAmount
    def getInfo(self):
        return "Snake, " + super().getInfo() + ", Venom: {} mg".format(self.venomAmount)
    def __le__(self, rhs):
        return self.venomAmount <= rhs.venomAmount
    def __ge__(self, rhs):
        return self.venomAmount >= rhs.venomAmount


s1 = Snake(3, 20.0, 50)
s2 = Snake(5, 10.5, 150)

assert s1.getInfo() == \
    "Snake, Age: 3 years, Weight: 20.0 lbs, Venom: 50 mg"
assert s2.getInfo() == \
    "Snake, Age: 5 years, Weight: 10.5 lbs, Venom: 150 mg"
assert (s1 <= s2) == True
assert (s2 <= s1) == False
s1.getInfo()

def computePower(base,power):
    if power == 0:
        return 1
    else:
        return base * computePower(base,power-1)
