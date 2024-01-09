#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? 

class Father:
    house=0
    bal=0

    def getdata(self):
     self.car=input("Enter the number of house: ")
     self.bal=input("Enter your bank details: ")

class Son(Father):
    def printdata(self):
        print("house: ",self.car)
        print("Bank Balance: ",self.bal)

n=Son()
n.getdata()
n.printdata()