import random 
choice=int(input("ENter 1 for code and 2 for decode: "))
if(choice==1):
    word=input("Enter Text you want to send : ")
    a=word.split(" ")
    nwords=[]
    for s in a:
        if(len(s)>2):
            f=s[0]
            s=s[1:]
                 
            test_strings = ["abc", "xyz", "mno", "pqr", "uvw", "def", "ghi", "jkl", "stu", "vwe"]
            nwords.append(random.choice(test_strings)+s+f+random.choice(test_strings))
        else:
           nwords.append(s[::-1])
    print(" ".join(nwords))

elif(choice==2):
     word=input("Enter Text you want to send : ")
     a=word.split(" ")
     nwords=[]
     for s in a:
        if(len(s)>8):        
            a=s[3:-3]
            f=a[len(a)-1]
            nwords.append(f+a[0:len(a)-1])
        else:
           
           nwords.append(s[::-1])
     print(" ".join(nwords))
   
else:
    print("Wrong choice choose from 1 & 2 !!")
     
