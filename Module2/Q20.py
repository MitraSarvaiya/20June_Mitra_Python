str=["Python", "Java", "PHP", "C++"]

x=len(str[0])
y=str[0]

for i in str:
    if(len(i)>x):
        x=len(i)
        y=i
print("The Longest Length Word Is:",y)
print("Length:",x)