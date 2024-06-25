#Q7 Write a Python program to read a file line by line store it into a variable.

f1 = open('student.txt','r+')
readline = f1.readlines()
filecontant = ""
for line in readline:
    filecontant+=line
print(filecontant)    