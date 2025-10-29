# Q.1 WAP to check if a number entered by the user is odd or even
number = int(input("Enter number:"))
if(number%2==0):
    print("number is even")
else:
    print("number is odd")

# Q.2 WAP to find the gratest of 3 number entered by the user     
    
# Q.3 WAP to find the number is multiple of 7 or not
digit=int(input("Enter one number: "))
if(digit%7==0):
   print("Enter number is multiple of 7")  
else:
    print("Enter number is not multiple of 7")       

# Q.4 WAP to input user's first name & print its length    
name = str(input("Enter your first name: "))    
lengthOfName = len(name)
print("length of first name is",lengthOfName)

# Q.5 WAP to find the occurence of '$' in a String
str = str(input("Enter a string: "))
occurence = str.count('$')
print("occurence of given number is: ",occurence)

