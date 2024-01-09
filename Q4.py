#Write a Python program to read first n lines of a file.

f1=open("Q4.txt",'a')
f1.write(''' Name: Mitra.
City: Rajkot.
Subject: Python
Mobile no.: 9624116167''')
f1.close()
x=open("Q4.txt",'r')
print(x.readlines()[:5])