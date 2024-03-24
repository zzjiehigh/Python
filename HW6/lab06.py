from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i = i + 1
            else:
                apartmentList[k] = righthalf[j]
                j = j +1
            k = k + 1
        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i +1
            k = k +1
        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1

def ensureSortedAscending(apartmentList):
    Done = True
    i = 1
    while Done == True and i < len(apartmentList):
        if apartmentList[i - 1] > apartmentList[i]:
            Done = False
        i += 1
    return Done

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[len(apartmentList)-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    aff_apart = ""
    mergesort(apartmentList)
    for i in apartmentList:
        if i.getRent() <= budget:
            aff_apart += i.getApartmentDetails()
            aff_apart += "\n"
    return aff_apart[:-1]


