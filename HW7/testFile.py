from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue
from OrderQueue import QueueEmptyException
import pytest

def test_Pizza():
    p = Pizza("S")
    assert p.getSize() == "S"
    assert p.getPrice() == 0
    p.setPrice(10)
    p.setSize("L")
    assert p.getSize() == 'L'
    assert p.getPrice() == 10

def test_CustomPizza():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: S\nToppings:\nPrice: $8.00\n"
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $14.00\n"

def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == "SPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n"
    assert sp1.getPrice() == 12
    assert sp1.getSize() == "S"

def test_PizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    assert order.getOrderDescription() == "******\nOrder Time: 123000\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ extra cheese\n\t+ sausage\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: S\nName: Carne-more\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $21.00\n******\n"

def test_OrderQueue():
    cp1 = CustomPizza("S")
    cp1.addTopping("extracheese")
    cp1.addTopping("sausage")
    sp1=SpecialtyPizza("S","Carne-more")
    cp2=CustomPizza("M")
    cp2.addTopping("extracheese")
    cp3=CustomPizza("L")
    order1 = PizzaOrder(123000)
    order1.addPizza(cp1)
    order1.addPizza(sp1)
    order2 = PizzaOrder(800)
    order2.addPizza(cp2)
    order3 = PizzaOrder(131423)
    order3.addPizza(cp3)
    oq = OrderQueue()
    oq.addOrder(order1)
    oq.addOrder(order2)
    oq.addOrder(order3)
    assert oq.processNextOrder() == "******\nOrder Time: 800\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ extracheese\nPrice: $10.75\n\n----\nTOTAL ORDER PRICE: $10.75\n******\n"

with pytest.raises(QueueEmptyException):
    oq = OrderQueue()
    oq.processNextOrder()
