str=input("Enter a string: ")
str2=""

if len(str) < 2:
    print("New string: ",str2)
else:
    str2=str[:2] + str[-2:]
    print("New string:",str2)

