class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}"\
               .format(self.rent, self.metersFromUCSB, self.condition)

    def __gt__(self, other):
        if self.rent == other.rent:
            if self.metersFromUCSB == other.metersFromUCSB:
                return -len(self.condition) > -len(other.condition)
            else:
                return self.metersFromUCSB > other.metersFromUCSB
        else:
            return self.rent > other.rent

    def __lt__(self, other):
        if self.rent == other.rent:
            if self.metersFromUCSB == other.metersFromUCSB:
                return -len(self.condition) < -len(other.condition)
            else:
                return self.metersFromUCSB < other.metersFromUCSB
        else:
            return self.rent < other.rent

    def __eq__(self, other):
        if self.rent == other.rent:
            if self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == other.condition:
                    return True
        return False


