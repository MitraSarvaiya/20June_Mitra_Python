#Q28 What is used to check whether an object o is an instance of class A?

class A():
    def get_data(self):
        city = input("Enter the city of the person :")
        name = (input("Enter the name of the person :"))
        print("City : ",city)
        print("Name : ",name)

o = A()
if isinstance(o,A):
    print("O is instance")
else:
    print("O is not an instance")       