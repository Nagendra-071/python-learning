import random
import time
lisT=[['Draw','Win','Lose'],
      ['Lose','Draw','Win'],
      ['Win','Lose','Draw']]

computer=[0,1,2]
points=0
print("WELCOME TO SANKE, WATER, GUN GAME!! \n ")
for i in range(10):
    print("\n")
    print(f"Round {i}  of 10!!!")
    player=int(input("Enter 0 for SNAKE ,1 for WATER and 2 for GUN and 3 for exit: "))
    
    if(player>3 | player<0) :
       print("Invalid input!!")

    elif(player==3):
        print("Result are being calculated....")
        time.sleep(2)
        print(f"Your Score is : {points}    ||      Computer Socre is : {10-points}")   
        time.sleep(2)
        print("Exited from  the game ")
        break
     
    
    else:
        comp_choice=random.choice(computer)
        print(f"Computer Chose Snake  {{1}} ")if(comp_choice==0)else print(f"Computer Chose Water  {{1}}")if(comp_choice==1)else print(f"Computer Chose Gun  {{2}}")
        outcome=lisT[player][comp_choice]
    
        if(outcome=="Draw"):
            print("It's a Draw!")
            points+=0
        elif(outcome=="lose"):
            print("Your Lose!")
            points+=0
        else:
            print("You Win")
            points+=1
    

        
        
        
        
    

