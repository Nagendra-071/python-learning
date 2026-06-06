import time
print(time.time())

time.sleep(4)
print("time is returned in sec and wait time is 4 sec")
t=time.localtime()
formatt=time.strftime("%Y-%m-%d %H %M %S ",t)
print(formatt)