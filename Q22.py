#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class.












class Student:
    def __init__(self, name, Contact, Subject):
        self.name = name
        self.contact = Contact
        self.sub = Subject
        
    def get_info(self):
        return f"Name: {self.name}, Contact: {self.contact}, Subject: {self.sub}"


student1 = Student("Mitra", 9624116167, "Python" )



print(student1.get_info())
