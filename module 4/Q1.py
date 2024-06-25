#Q1 What is File function in python? What is keywords to create and write file

"""The File function in Python is a function that allows you to open and read files. It takes two arguments: the name of the file you want to open, 
and the mode in which you want to open it. 
The mode can be either 'r' for reading, 'w' for writing, or 'a' for appending. To create a file in Python, you can use the open() function with 
the 'w' mode.  This will create a new file if it does not exist, and overwrite the contents of the file if it does exist.
To write to a file in Python, you can use the write() function. This function takes two arguments: the string you want to write to the file, 
and the file object that you want to write to."""

"""Here are some of the keywords that you can use to create and write to a file in Python:

open() - Opens a file for reading, writing, or appending.
write() - Writes a string to a file.
close() - Closes a file.
read() - Reads a string from a file.
seek() - Moves the file pointer to a specific position in the file.
tell() - Returns the current position of the file pointer."""

# Create a file object
f = open('student.txt', 'w')

# Write to the file
f.write('This is my file.')

# Close the file
f.close()
