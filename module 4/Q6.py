#Q6 Write a Python program to read a file line by line and store it into a list

f1 = open('student.txt','r+')
read_lines = f1.readlines()
file_list = []
for line in read_lines:
    file_list.append(line)
  