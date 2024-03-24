from Car import Car

class CarInventoryNode:
    def __init__(self,car,left=None,right=None, parent=None):
        self.car = car
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]
        self.left = left
        self.right = right
        self.parent = parent
	
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        if self.parent== None:
            self.parent = parent
        else:
            a = parent
            a.parent = self.parent
            self.right = a

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        if self.left== None:
            self.left = left
        else:
            a = left
            a.left = self.parent
            self.left = a           

    def getRight(self):
        return self.right

    def is_left(self):
        return self.parent and self.parent.left == self
    
    def is_right(self):
        return self.parent and self.parent.right == self

    def setRight(self, right):
        if self.right == None:
            self.right = right
        else:
            a = right
            a.right = self.right
            self.right = a

    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.right or self.left)
    
    def hasBothChildren(self):
        return self.right and self.left

    def hasAnyChildren(self):
        return self.right or self.left
	    
    def  __str__(self):
        result = []
        for car in self.cars:
            result.append(str(car))
            result.append('\n')
        return "".join(result)
    
    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
        return False

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
        return False

    def __eq__(self, rhs):
        if rhs == None:
            return False
        else:
             return self.make == rhs.make and self.model == rhs.model

    def _inOrder(self):
        ret=""
        if self != None:
            if self.left != None:
                ret += str(self.left._inOrder())
            ret += str(self)
            if self.right != None:
                ret += str(self.right._inOrder())
        return ret

    def _postOrder(self):
        ret=""
        if self != None:
            if self.left != None:
                ret += str(self.left._postOrder())
            if self.right != None:
                ret += str(self.right._postOrder())
            ret += str(self)
        return ret
    def _preOrder(self):
        ret=""
        if self != None:
            ret += str(self)
            if self.left != None:
                ret += str(self.left._preOrder())
            if self.right != None:
                ret += str(self.right._preOrder())
        return ret
    
    def replaceNodeData(self,cars,make, model,lc,rc):
        self.cars = cars
        self.make = make
        self.model = model 
        self.left = lc
        self.right = rc
        if self.getLeft():
            self.left.parent = self
        if self.getRight():
            self.right.parent = self
            
    def findSuccessor(self):
        node = self
        succ = None
        if self.getRight():
            succ = self.getRight().findMin()
        else:
            if self.getParent():
                if self.getParent().getLeft() == self:
                    succ = self.getParent()
                else:
                    self.parent.right = None
                    succ = self.getParent().findSuccessor()
                    self.parent.setRight(node)
        return succ

    def findMin(self):
        current = self
        while current.getLeft():
            current = current.left
        return current
    
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
