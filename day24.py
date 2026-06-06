tup=(1,2,3,4)  
#tupper use() while lis use []
print(tup)
#for making changes in tuple

temp=list(tup)
temp.append("Aus")
temp[2]=34
tup=tuple(temp)
print (tup)
print(tup.count(34)) 