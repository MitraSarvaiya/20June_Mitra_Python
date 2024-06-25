#Q10 Write a Python program to count the frequency of words in a file. 

file = open('student.txt','r+')
read_line = file.readlines()
word_count = {}
for line in read_line:
    word = line.split()
    for j in word:
        if j in word_count:
            word_count[j]+=1
        else:
            word_count[j]=1    
for word,count in word_count.items():
    print(f"{word} : {count}")        
