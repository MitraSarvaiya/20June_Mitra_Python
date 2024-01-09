# Write a Python program to write a list to a file.


    
x = open("Q4.txt", 'a')

my_list = ['My Father name is Bhaveshbhai.', 'My Brother name is Daksh.', 'My Mother name is Bhavikaben.']

x.write('\n')
for item in my_list:
    x.write(f'{item}\n')

x.close()