from Apartment import Apartment
from lab06 import mergesort
from lab06 import ensureSortedAscending
from lab06 import getBestApartment
from lab06 import getWorstApartment
from lab06 import getAffordableApartments

a0 = Apartment(1200, 200, "average")
a1 = Apartment(1200, 200, "excellent")
a2 = Apartment(1000, 100, "average")
a3 = Apartment(1000, 215, "excellent")
a4 = Apartment(700, 315, "bad")
a5 = Apartment(800, 250, "excellent")
apartmentList = [a0, a1, a2, a3, a4, a5]

def test_gt():
    assert (a0 > a1) == True
    assert (a1 > a2) == True
    assert (a2 > a3) == False
    assert (a3 > a4) == True

def test_lt():
    assert (a0 < a1) == False
    assert (a1 < a2) == False
    assert (a2 < a3) == True
    assert (a3 < a4) == False

def test_eq():
    assert (a0 == a0) == True
    assert (a1 == a1) == True
    assert (a2 == a3) == False
    assert (a3 == a4) == False
    
def test_mergesort_and_ensureSortedAscending():
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    L1 = [a3, a5, a0, a2, a4, a1]
    assert ensureSortedAscending(L1) == False
    mergesort(L1)
    assert ensureSortedAscending(L1) == True

def test_getBestApartment():
    L1 = [a3, a5, a0, a2, a4, a1]
    L2 = [a0, a1, a2, a3, a4, a5]
    L3 = [a0, a0, a2, a2, a3, a3]
    assert getBestApartment(L1) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    assert getBestApartment(L2) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    assert getBestApartment(L3) == "(Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: average"

def test_getWorstApartment():
    L1 = [a3, a1, a1, a2, a1, a1]
    L2 = [a4, a4, a2, a3, a2, a5]
    L3 = [a0, a0, a2, a2, a3, a3]
    assert getWorstApartment(L1) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: excellent"
    assert getWorstApartment(L2) == "(Apartment) Rent: $1000, Distance From UCSB: 215m, Condition: excellent"
    assert getWorstApartment(L3) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"

def test_getAffordableApartments():
    assert getAffordableApartments(apartmentList, 1000) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad\n(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent\n(Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: average\n(Apartment) Rent: $1000, Distance From UCSB: 215m, Condition: excellent"
    assert getAffordableApartments(apartmentList, 800) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad\n(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent"
    assert getAffordableApartments(apartmentList, 200) == ""
    
