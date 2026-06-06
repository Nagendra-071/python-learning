a=input("NUmber b/w 5 and 9: ")
if(a=='quit'):
    print("Exiting....")
    
else:
    
    if(int(a)<5  or int(a)>9):
        raise ValueError("Value in not in specified range ")
    
    
 