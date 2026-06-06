def cube(x):
    return x*x*x

l=[1,2,3,4,5,6,7]
# newl=[]
# for item in l :
#     newl.append(cube(item))

newl=list(map(cube,l))    
print(newl)
    
    
#FILTER

def filter_fun(a):
    return a>4

newnewl=list(filter(filter_fun,l))
print(newnewl)

#REDUCE
from functools import reduce

total = reduce(lambda x, y: x + y, l)
print(total)

print(l[0] is l[1])