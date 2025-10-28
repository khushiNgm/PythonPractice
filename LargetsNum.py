# 5. Find the largest of three numbers
a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
c= int (input("Enter the value of c: "))
if a>b:
    if a>c:
        print(f"a is greatest: {a}")
    else:
        print(f"c is greatest: {c}")    
else:
    if b>c:
        print(f"b is greatest{b}")
    else:
        print(f"c is greatest {c}")            

#Type 2
a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
c= int (input("Enter the value of c: "))  

greatest = max(a,b,c)
print(f"The greatest number is : {greatest}")      