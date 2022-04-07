email = input("Enter the email address to be validated")
# set some boolean variables (flags) for the things we are looking for
containsSpaces = False
containsAtSymbol = False
containsDot = False

#check if there is a space anywhere
if " " in email:
  containsSpaces = True

#loop through each character in the email
for char in email:
  #check if there is an @ and set the flag to True
  if char == "@":
    containsAtSymbol = True
  #check if it is a dot and there is already an @ symbol found (ie dot is after the @) 
  if char == "." and containsAtSymbol == True:
    containsDot = True

# check the 3 conditions
# can also be written more consisely as
# if not containsSpaces and containsAtSymbol and containsDot:
if containsSpaces == False and containsAtSymbol == True and containsDot == True:
  print("email IS valid")
else:
  print("email is NOT valid")