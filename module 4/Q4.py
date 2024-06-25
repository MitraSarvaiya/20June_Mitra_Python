#Q4 Write a Python program to read first n lines of a file. 

f1=open('student.txt','r+')

n = int(input("Enter the number of lines to print: "))
lines = f1.readlines()
for i in range(n):
    print(lines[i])