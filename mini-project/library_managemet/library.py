from book import Book

class LibraryManager( object ):
    def __init__( self ):
        self.books = {}

    def createBook( self, id, name, author ):
        book = Book( id, name )
        self.books[id] = book

    def updateBook( self, id, name, author ):
        pass

    def displayBooks( self ):
        pass

libraryManager = LibraryManager()

libraryManager.createBook(1,'CSLR','Cormen')

libraryManager.displayBooks()