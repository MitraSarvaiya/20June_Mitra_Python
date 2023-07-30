#Write python program that swap two number with temp variable and without temp variable.


a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print("A:", a)
print("b:", b)


#without tmp
a,b=b,a
print("A:", a)
print("B:", b)

#withtmp
tmp=a 
a=b 
b=tmp 


print("A:",a)
print("B:",b)