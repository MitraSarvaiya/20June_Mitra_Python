#What is File function in python? What is keywords to create and write file. 
"""Python file object provides methods and attributes to access and manipulate files. Using file objects, we can read or write any files. 
Whenever we open a file to perform any operations on it, Python returns a file object."""




f1=open("python.txt",'w')
f1.write("hello python!!!")
print(f1)