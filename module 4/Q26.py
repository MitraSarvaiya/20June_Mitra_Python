#Q26 Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? 

"""Inheritance relationship defines the classes that inherit from other classes as derived, subclass, or sub-type classes.
Base class remains to be the source from which a subclass inherits. """

#example
class Person():
    
    fname=""
    lname= ""

class teacher(Person):
    
    def getdata(self):
        self.fname = input("Enter First name : ")
        self.lname = input("Enter Last name  : ")

    def printdata(self):
        print(self.fname , self.lname)
        

p1 = teacher()
p1.getdata()
p1.printdata()            