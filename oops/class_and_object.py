id = 1

class Patient( object ):
    def __init__( self, id, name='Alex', age=85 ):
        #This is the constructor of the object
        self.name = name
        self.age  = age
        self.id   = id

    def printDetails( self ):
        print('Name:'+self.name)
        print('Age:'+str(self.age))

p1 = Patient(id)
p1.printDetails()

id += 1
p2 = Patient(id,'Bob',67)
p2.printDetails()