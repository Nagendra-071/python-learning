x=4

match x:
    case 0: 
        print("zero")
    
    case 4 if(x%4==0):
        print("four")
        
    case _: 
        print("other number")
        
