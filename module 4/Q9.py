#Q9 Write a Python program to count the number of lines in a text file. 

file = open('student.txt','r+')

line = file.readlines()

count = 0
for lines in line:
    count+=1


print(count)    