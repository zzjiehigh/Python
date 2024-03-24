class Car:
    def __init__(self, make, model, year, price):
        self.make = str(make).upper()
        self.model = str(model).upper()
        self.year = year
        self.price = price

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def __gt__(self, other):
        if self.make == other.make:
            if self.model == other.model:
                if self.year == other.year:
                    return self.price > other.price
                else:
                    return -(self.year) > -(other.year)
            else:
                return self.model > other.model
        else:
            return self.make > other.make

    def __lt__(self, other):
        if self.make == other.make:
            if self.model == other.model:
                if self.year == other.year:
                    return self.price < other.price
                else:
                    return -(self.year) < -(other.year)
            else:
                return self.model < other.model
        else:
            return self.make < other.make

    def __eq__(self, other):
        if self.make == other.make:
            if self.model == other.model:
                if self.year == self.year:
                    if self.price == other.price:
                        return True
        return False
    
    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}" \
               .format(self.make, self.model, self.year, self.price)
