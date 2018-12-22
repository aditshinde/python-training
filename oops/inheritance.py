class Add( object ):
    def add( self, num1, num2 ):
        return num1 +  num2 + 100

class Subtract( object ):
    def subtract( self, num1, num2 ):
        return num1 - num2

class Multiply( object ):
    def multiply( self, num1, num2 ):
        return num1 * num2

class Divide( object ):
    def divide( self, num1, num2 ):
        return num1 / num2

class Arithmetic( Add, Subtract, Multiply, Divide ):
    def __init__( self, num1=0, num2=0 ):
        self.num1 = num1
        self.num2 = num2
        super( Add, self )

a = Arithmetic()
print(a.add(14,5))