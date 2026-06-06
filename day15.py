import time

timestamp= int(time.strftime('%H'))

if(timestamp<12):
    print("Good Morning!")
    
elif(timestamp>=12 | timestamp<16) :
    print("Good Afternoon!")

elif(timestamp>=16| timestamp<19) :
    print("Good Noon!")
    
else:
    print("Good Night!")    

       