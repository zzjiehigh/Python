from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None
        self.totalP = 0

    def addCar(self, car):
        if self.root:
            self._add(car, self.root)
        else:
            self.root = CarInventoryNode(car)
        self.totalP += car.price

    def _add(self, car, currentNode):
        if CarInventoryNode(car) < currentNode:
            if currentNode.getLeft():
                self._add(car, currentNode.left)
            else:
                currentNode.left = \
				CarInventoryNode(car,parent=currentNode)
        elif CarInventoryNode(car) > currentNode:
            if currentNode.getRight():
                self._add(car, currentNode.right)
            else:
                currentNode.right = \
				CarInventoryNode(car,parent=currentNode)
        else:
            currentNode.cars.append(car)

    def doesCarExist(self, car):
        if self.root:
            ret = self._get(car, self.root)
            if ret:
                return True
            else:
                return False
        else:
            return False

    def inOrder(self):
        if self.root == None:
            return ""
        return self.root._inOrder()

    def postOrder(self):
        if self.root == None:
            return ""
        return self.root._postOrder()

    def preOrder(self):
        if self.root == None:
            return ""
        return self.root._preOrder()

    def _get(self, car, currentNode):
        if not currentNode:
            return None
        elif car in currentNode.cars:
            return True
        elif CarInventoryNode(car) < currentNode:
            return self._get(car, currentNode.left)
        elif CarInventoryNode(car) > currentNode:
            return self._get(car, currentNode.right)

    def getBestCar(self, make, model):
        if self.root:
            cars = self._getSame(make, model, self.root)
            if cars:
                a = cars[0]
                for i in cars:
                    if i > a:
                        a = i
                return a
            else:
                return None
        else:
            return None

    def getWorstCar(self, make, model):
        if self.root:
            cars = self._getSame(make, model, self.root)
            if cars:
                z = cars[0]
                for i in cars:
                    if i < z:
                        z = i
                return z
            else:
                return None
        else:
            return None

    def _getSame(self, make, model, currentNode):
        if not currentNode:
            return None
        elif model.upper() == currentNode.model and make.upper() == currentNode.make:
            return currentNode.cars
        elif make.upper() < currentNode.make or (make.upper() == currentNode.make and model.upper() < currentNode.model):
            return self._getSame(make, model, currentNode.left)
        else:
            return self._getSame(make, model, currentNode.right)
        
    def _getSameNode(self, make, model, currentNode):
        if not currentNode:
            return None
        elif model.upper() == currentNode.model and make.upper() == currentNode.make:
            return currentNode
        elif make.upper() < currentNode.make or (make.upper() == currentNode.make and model.upper() < currentNode.model):
            return self._getSameNode(make, model, currentNode.left)
        else:
            return self._getSameNode(make, model, currentNode.right)

    def getTotalInventoryPrice(self):
        return self.totalP

    def getSuccessor(self, make, model):
        if self.root:
            node = self._getSameNode(make, model, self.root)
            if node:
                return node.findSuccessor()
        else:
            return None

    def removeCar(self, make, model, year, price):
        node = self._getSameNode(make, model, self.root)
        if node:
            cars = self._getSame(make, model, self.root)
            car = Car(make, model, year, price)
            if car in cars:
                cars.remove(car)
                if len(cars) == 0:
                    if node.isLeaf():
                        if node.isRoot():
                            node = None
                        else:
                            if node == node.parent.left:
                                node.parent.left = None
                            else:
                                node.parent.right = None
                    elif node.hasBothChildren():
                        succ = node.findSuccessor()
                        succ.spliceOut()
                        node.cars = succ.cars
                        node.make = succ.make
                        node.model = succ.model
                    else:
                        if node.getLeft():
                            if node.is_left():
                                node.left.parent = node.parent
                                node.parent.left = node.left
                            elif node.is_right():
                                node.left.parent = node.parent
                                node.parent.right = node.left
                            else:
                                node.replaceNodeData(node.left.cars,
                                                     node.left.make,
                                                     node.left.model,
                                                     node.left.left,
                                                     node.left.right)
                        else:
                            if node.is_left():
                                node.right.parent = node.parent
                                node.parent.left = node.right
                            elif node.is_right():
                                node.right.parent = node.parent
                                node.parent.right = node.right
                            else:
                                node.replaceNodeData(node.right.cars,
                                                     node.right.make,
                                                     node.right.model,
                                                     node.right.left,
                                                     node.right.right)
                return True
            else:
                return False
        else:
            return False
