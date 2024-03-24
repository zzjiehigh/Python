class Car:
    def __init__(self, make, model, year, price):
        self.make = str(make).upper()
        self.model = str(model).upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
            elif self.model == rhs.model:
                if self.year > rhs.year:
                    return True
                elif self.year == rhs.year:
                    return self.price > rhs.price
        return False

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
            elif self.model == rhs.model:
                if self.year < rhs.year:
                    return True
                elif self.year == rhs.year:
                    return self.price < rhs.price
        return False

    def __eq__(self, rhs):
        if rhs == None:
            return False
        else:
            return self.make == rhs.make and self.model == rhs.model and self.year == rhs.year and self.price == rhs.price
    
    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}" \
               .format(self.make, self.model, self.year, self.price)
