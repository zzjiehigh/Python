from Book import Book
from BookCollectionNode import BookCollectionNode
class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count +1
            temp = temp.getNext()
        return count
    
    def insertBook(self, book):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() > book:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        temp = BookCollectionNode(book)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
    def getBooksByAuthor(self, author):
        temp = self.head
        book = ""
        while temp != None:
            if temp.getData().getAuthor().lower() == author.lower():
                book += temp.getData().getBookDetails()
                book += "\n"
            else:
                book
            temp = temp.getNext()
        return book
    def getAllBooksInCollection(self):
        temp = self.head
        collection = ""
        while temp != None:
            collection += temp.getData().getBookDetails()
            collection += "\n"
            temp = temp.getNext()
        return collection
        
    def removeAuthor(self, author):
        current = self.head
        while current.getData().getAuthor().lower() == author.lower():
            self.head = current.getNext()
            current = self.head
        while current.getNext() != None:
            if current.getNext().getData().getAuthor().lower() == author.lower():
                current.setNext(current.getNext().getNext())
            else:
                current = current.getNext()

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        elif bookNode.getData().getTitle().lower() == title.lower():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())





