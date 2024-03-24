from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

car1 = Car("Nissan", "Leaf", 2018, 18000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("Mercedes", "Sprinter", 2022, 40000)
car4 = Car("Mercedes", "Sprinter", 2014, 25000)
car5 = Car("Ford", "Ranger", 2021, 25000)

def test_Car():
    assert (car1 > car2) == False
    assert (car4 > car3) == True
    assert (car1 < car2) == True
    assert (car4 < car3) == False
    assert (car3 == car3) == True
    assert car1.__str__() == 'Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000'
    assert car2.__str__() == 'Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000'

def test_CarInventoryNode():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    carNode2 = CarInventoryNode(car3)
    carNode3 = CarInventoryNode(car4)
    carNode4 = CarInventoryNode(car5)
    assert str(carNode) == 'Make: DODGE, Model: DART, Year: 2015, Price: $6000\nMake: DODGE, Model: DART, Year: 2003, Price: $5000\n'
    assert carNode.getMake() == 'DODGE'
    assert carNode.getModel() == 'DART'
    assert carNode.getParent() == None
    assert carNode.getLeft() == None
    assert carNode.getRight() == None
    carNode.setParent(carNode2)
    carNode.setLeft(carNode3)
    carNode.setRight(carNode4)
    assert carNode.getParent() == carNode2
    assert carNode.getLeft() == carNode3
    assert carNode.getRight() == carNode4


def test_CarInventory():
    bst = CarInventory()
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car5) == False
    bst.addCar(car5)
    assert bst.inOrder() == "Make: FORD, Model: RANGER, Year: 2021, Price: $25000\nMake: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\nMake: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\nMake: NISSAN, Model: LEAF, Year: 2018, Price: $18000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"
    assert bst.postOrder() == "Make: FORD, Model: RANGER, Year: 2021, Price: $25000\nMake: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\nMake: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\nMake: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n"
    assert bst.preOrder() == "Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\nMake: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\nMake: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\nMake: FORD, Model: RANGER, Year: 2021, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"
    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Ford", "Ranger") == car5
    assert bst.getBestCar("a", "Acd") == None
    assert bst.getWorstCar("Tesla", "Model3") == car2
    assert bst.getWorstCar("Ta", "Model3") == None
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    car6 = Car("Dodge", "dart", 2003, 6000)
    car7 = Car("dodge", "DaRt", 2003, 5000)
    bst.addCar(car6)
    bst.addCar(car7)
    assert bst.getWorstCar("Dodge", "dart") == car7
    assert bst.getTotalInventoryPrice() == 169000

def test_CarInventory_new():
    bst = CarInventory()
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getSuccessor("Mazda", "CX-5") == car2
    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.inOrder() == 'Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: BMW, Model: X5, Year: 2022, Price: $60000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n'
    bst.removeCar("BMW", "X5", 2022, 60000)
    assert bst.inOrder() == 'Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: MAZDA, Model: CX-5, Year: 2022, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n'
    bst.removeCar("Mazda", "CX-5", 2022, 25000)
    assert bst.inOrder() == 'Make: AUDI, Model: A3, Year: 2021, Price: $25000\nMake: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n'
    bst.removeCar("Audi", "A3", 2021, 25000)
    assert bst.inOrder() == 'Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n'



