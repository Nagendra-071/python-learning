a=float(input("Enter no:"))
b=float(input("Enter no:"))
operator=input("Choose operation(/,*,+,-) : ")

if(operator=="/"):    
    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(a / b)
        
if(operator=="+"):
    print(a+b)
    
if(operator=="-"):
    print(a-b)
    
if(operator=="*"):
    print(a*b)
     