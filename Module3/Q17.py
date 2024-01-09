#When is the finally block executed?

"""The finally statement is always carried out following the try statement.
If an exception was not handled by the except block, it is raised again after the finally block has been executed.
-> Following is the execution order:-
    1. The try block's code is executed.   
    2. If an exception is raised while the try block is running, the associated catch block is run, if necessary.
    3. Regardless of whether an exception occurred or not, the code contained in the finally block is carried out.
"""

try:
    result = 10 / 0  
except ZeroDivisionError:
    print("Division by zero error")
finally:
    print("This will always execute")
