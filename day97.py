import threading
import time

def func(seconds):
    print("Sleeping for  {seconds} seconds.")
    time.sleep(seconds)
    
    


t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])
