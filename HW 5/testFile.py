from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection
b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)

def test_Book():
    assert b1.getTitle() == 'The Shining'
    assert b2.getAuthor() == 'Cline, Ernest'
    assert b3.getYear() == 1977
    assert b0.getBookDetails() == 'Title: Cujo, Author: King, Stephen, Year: 1981'
    assert b1.getBookDetails() == 'Title: The Shining, Author: King, Stephen, Year: 1977'
    assert (b0 > b1) == True
    assert (b2 > b3) == False

def test_BookCollectionNode():
    n = BookCollectionNode(b1)
    assert n.getNext() == None

def test_isEmpty():
    bc = BookCollection()
    assert bc.isEmpty() == True
    bc.insertBook(b1)
    assert bc.isEmpty() == False

def test_getNumberOfBooks():
    bc = BookCollection()
    assert bc.getNumberOfBooks() == 0
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b0)
    assert bc.getNumberOfBooks() == 3

def test_getBooksByAuthor():
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.getBooksByAuthor("KING, Stephen") == 'Title: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n'
    assert bc.getBooksByAuthor("Stephen") == ''

def test_getAllBooksInCollection():
    bc = BookCollection()
    assert bc.getAllBooksInCollection() == ''
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.getAllBooksInCollection() == 'Title: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n'
    
def test_removeAuthor():
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b2)
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011\nTitle: Cujo, Author: King, Stephen, Year: 1981\n'
    bc.removeAuthor('King, Stephen')
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n'
    bc.removeAuthor('Cline, Ernest')
    assert bc.getAllBooksInCollection() == ''

def recursiveSearchTitle():
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False
    assert bc.recursiveSearchTitle("fvbn", bc.head) == False


