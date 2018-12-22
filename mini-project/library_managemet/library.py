from book import Book
from pprint import pprint
import csv

class LibraryManager( object ):
    def __init__( self ):
        self.books = {}

    def createBook( self, id, name, author, price ):
        book = Book( id, name, author, price )
        self.books[id] = [book,'','']

    def updateBook( self, id, name, author, price ):
        book = Book( id, name, author, price )
        self.books[id] = [book,'','']

    def displayBooks( self ):
        for item in self.books:
            b = self.books[item][0]
            print('ID: ',b.id)
            print('Name: ',b.name)
            print('Author: ',b.author)
            print('Price: ',b.price)

    def issueBook( self, id, rollno, doi ):
        for item in self.books:
            if item == id:
                self.books[item][1] = rollno
                self.books[item][2] = doi

    def writeOut( self ):
        with open('Library.csv','w') as out:
            csvWriter = csv.writer(out)
            
            for item in self.books:
                b = self.books[item][0]
                rno = self.books[item][1]
                doi = self.books[item][2]

                row = (b.id,b.name,b.author,b.price,rno,doi)
                
                csvWriter.writerow(row)

libraryManager = LibraryManager()

libraryManager.createBook(1,'CSLR','Cormen',600.0)
libraryManager.createBook(2,'CSLR','Cormen',600.0)
libraryManager.createBook(3,'Headfirst Java','O\'Rielly',100.0)
libraryManager.createBook(4,'C for Dummies','Pearson',1200.0)
libraryManager.createBook(5,'C for Dummies','Pearson',1200.0)

#libraryManager.displayBooks()

libraryManager.updateBook(2,'Harry Potter', 'J. K. Rowling', 750.0)

#libraryManager.displayBooks()

libraryManager.issueBook(3,'45','2018-12-21')

pprint(libraryManager.books)

libraryManager.writeOut()