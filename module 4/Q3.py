#Q3 Write a Python program to append text to a file and display the text
 
f1 = open('student.txt','a')
def appenddata():
    n=int(input("number of students : "))
    for i in range(n):
        name = input(f"Enter Name Of Student{i+1}: ")
        city = input(f"Enter city Of student {i+1}: ")
        f1.write("\n")
        f1.write(f"NAME = {name}\n")
        f1.write(f"CITY = {city}\n")
        f2 = open('student.txt','r+')
        print(f2.read())

appenddata()
