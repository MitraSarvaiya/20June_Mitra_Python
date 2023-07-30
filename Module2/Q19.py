x=input("Enter a string:")

if len(x):
    y=(x.replace('not','good') + x.replace('poor','good'))
    print(y)