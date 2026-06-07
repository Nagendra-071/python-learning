#used to print value of i every time called witohut storing any where 
#allows ro generate value on the fly(mauke pe)
def my_generator():
    for i in range(500000):
        yield i

gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
