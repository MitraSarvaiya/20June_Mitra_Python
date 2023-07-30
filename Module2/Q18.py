str=input("Enter a string")

if str.endswith('ing'):
  str += 'ly'
elif len(str) >= 3:
  str += 'ing'

print(str)