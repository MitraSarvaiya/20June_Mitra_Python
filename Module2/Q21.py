str=input("Enter a string:")

if len(str) % 4 == 0:
    print(str[::-1])
else:
    print(str)
