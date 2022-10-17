num = int (input ("Enter any number to test whether it is odd or not"))  #Accept Number

if(num==0):  #Check condition for the zero
    print("Number must be positive or negative")
    
elif (num % 2) == 1:
    print("The number is odd ") #Check Condition for the Odd number. 
else:
    print("The provided number is not odd number")
