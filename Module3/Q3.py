#Write a Python program to append text to a file and display the text. 

from fileinput import close


f1=open("python.txt",'a')
f1.write("\nhello python!!!")
f1.close()

f2=open("python.txt",'r')
print(f2.read())