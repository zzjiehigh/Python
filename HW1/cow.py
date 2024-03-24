from Animal import Animal

class Cow(Animal):
    # Available method for the Cow Class
    def __init__(self, species = None, name = None, sound = None):
        super().__init__(species, name)
        self.sound = sound
    def setSound(self, sound):
        self.sound = sound
    def getSound(self):
        s = "Using super class getSound\n"
        s += Animal.getSound(self) + "\n"
        s += "Extending it with our getsound\n"
        s += "{}!!!".format(self.sound, self.sound)
        return s
    
c = Cow("Cow", "Betsy")
print(c.getAttributes())
c.setSound("Moo") # Sets a Cow sound attribute to "Moo"
print(c.getSound()) # I’m an Animal!!! (calls the Animal.getSound method)

a = Animal("Unicorn", "Lala")
print(a.getAttributes())
print(a.getSound()) # I’m an Animal!!!

c = Cow("Cow", "Betsy", "Moo") # Passes in data for Animal AND Cow
a = Animal("Unicorn", "Lala")

zoo = [c, a]

for i in zoo:
	print(i.getAttributes())
	print(i.getSound())
	print("---")
