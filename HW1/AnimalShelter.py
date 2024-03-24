# file containing a class definition for an AnimalShelter object.
from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.animalShelter = {}
        
    def addAnimal(self, animal):
        if self.animalShelter.get(animal.species) == None:
            self.animalShelter[animal.species] = []
            
        self.animalShelter[animal.species].append(animal)
        
    def removeAnimal(self, animal):
        if self.animalShelter.get(animal.species) != None:
            if self.doesAnimalExist(animal):
                self.animalShelter[animal.species].remove(animal)
                                                                   
    def removeSpecies(self, species):
        species = species.upper()
        if self.animalShelter.get(species) != None:
             del self.animalShelter[species]

    def getAnimalsBySpecies(self, species):
        species = species.upper()
        animals = ""
        if self.animalShelter.get(species) != None:
            for animal in self.animalShelter[species][:-1]:
                animals += animal.toString() + '\n'
            animals += self.animalShelter[species][-1].toString()
            return animals
        else:
            return animals
    def doesAnimalExist(self, animal):
        if self.animalShelter.get(animal.species) != None :
            if animal in self.animalShelter[animal.species]:
                return True
        return False

