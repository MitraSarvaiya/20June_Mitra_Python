#Q11 Write a Python program to write a list to a file.  

list = ["Grapes","Mango","Kiwi","Coconut"]
f1 = open('list.txt','a')
for word in list:
    f1.write(word)
    f1.write("\n")
f2 = open('list.txt','r+')
lines = f2.readlines()
for line in lines:
    print(line)