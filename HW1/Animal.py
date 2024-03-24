# file containing a class definition for an Animal object.
class Animal:
    def __init__(self, species = None, weight = None, age = None, name = None):
        if species == None:
            self.species = species
        else:
            self.species = str(species).upper()
        if name == None:
            self.name = name
        else:
            self.name = str(name).upper()
        self.weight = weight
        self.age = age
    def setSpecies(self, species):
        self.species = str(species).upper()
    def setWeight(self, weight):
        self.weight = weight
    def setAge(self, age):
        self.age = age
    def setName(self, name):
        self.name = str(name).upper()
    def toString(self):
        animal_str = "Species: " + self.species
        animal_str += ", Name: " + self.name
        animal_str += ", Age: " + str(self.age)
        animal_str += ", Weight: " + str(self.weight)
        return animal_str
    def getSound(self):
        return "I'm an Animal!!!"
    def getAttributes(self):
        return "Species: {}, Name: {}".format(self.species, self.name)
    def getInfo(self):
        return "Species: {}, Name: {}".format(self.species, self.name)
