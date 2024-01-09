
# Write a Python program to find the second smallest number in a list.

m=list()
a=int(input("Enter number of list: "))
for i in range(a):
    x=int(input("Enter number: "))
    m.append(x)
print(m)
m.sort()
d=m[1]
print(d)