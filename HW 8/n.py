                if self.getRight():
                    succ = self.right.findMax()
            return succ
        
    def findMax(self):
        current = self
        while current.getRight():
            current = current.right
        return current
    def removeCar(self, make, model, year, price):
        currentNode = self.root
        while currentNode:
            if currentNode.make == make.upper() and currentNode.model == model.upper() and currentNode.year == year and currentNode.price == price:
                if currentNode.isLeaf():
                    if currentNode == currentNode.parent.left:
                        currentNode.parent.left = None
                    else:
                        currentNode.parent.right = None
                elif currentNode.hasBothChildren():
                    succ = currentNode.getSuccessor()
                    succ.spliceOut()
                    currentNode.car = succ.car
                else:
                    if currentNode.getLeft():
                        if currentNode.is_left():
                            currentNode.left.parent = currentNode.parent
                            currentNode.parent.left = currentNode.left
                        elif currentNode.is_right():
                            currentNode.left.parent = currentNode.parent
                            currentNode.parent.right = currentNode.left
                        else:
                            currentNode.replaceNodeData(currentNode.left.car,              
					currentNode.left.left,
					currentNode.left.right)
                    else:
                        if currentNode.is_left():
                            currentNode.right.parent = currentNode.parent
                            currentNode.parent.left = currentNode.right
                        elif currentNode.is_right():
                            currentNode.right.parent = currentNode.parent
                            currentNode.parent.right = currentNode.right
                        else:
                            currentNode.replaceNodeData(currentNode.right.car,              
					currentNode.right.left,
					currentNode.tight.right)
    def spliceOut(self):
        if self.isLeaf():
            if self.is_left():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.getRight():
                if self.is_left():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
