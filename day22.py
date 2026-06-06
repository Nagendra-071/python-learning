l=[12,31,2,3]
l.sort(reverse=True)
print(l)
print(l[0])
m=l.copy()
print(m)
l.extend(m)
print(l) 