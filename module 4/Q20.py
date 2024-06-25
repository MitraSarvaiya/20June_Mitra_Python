#Q20  How Do You Handle Exceptions With Try/Except/Finally In Python?
      #Explain with coding snippets. 

"""If any exception occurs, the try clause will be skipped and except clause will run. If any exception occurs, but the except clause within the 
code doesn't handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops."""

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 