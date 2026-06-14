import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for  {seconds} seconds.")
    time.sleep(seconds)
    return seconds
    
def main():    
    time1=time.perf_counter()
    #Code using thread
    t1=threading.Thread(target=func,args=[4])
    t2=threading.Thread(target=func,args=[2])
    t3=threading.Thread(target=func,args=[1])
    t1.start()
    t2.start()
    t3.start()


    #join use krne se max (t1,t2,t3)time me execution hoga
    t1.join()
    t2.join()
    t3.join()

    time2=time.perf_counter()
    print(time2-time1)
    
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future=executor.submit(func,3)
        # print(future.result())
        # future=executor.submit(func,2)
        # print(future.result())
        # future=executor.submit(func,4)
        # print(future.result())
        
        l=[2,4,3,5]
        results=executor.map(func,l)
        
        for result in results:
            print(result)
    
    
    
    
    
    
    
poolingDemo()    