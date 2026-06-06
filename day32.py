s1={1,2,3,4,5,6}
s2={7,2,3,8,9}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
print(s1.intersection(s2))
s3=s1.difference(s2)
print(s3)   
print(s1.issuperset(s2))

#foradding single item use ad else use update for mutliple
s1.add("hiro")
print (s1)