set1={1,2,3,4,5,6}
set2={4,5,6,7,8}

print(set1|set2)   
#print(set1.union(set2))

print(set1&set2)
#print(set1.intersection(set2))

print(set1-set2)
#print(set1.difference(set2))


s=set()
s.update(range(5,20))
print(s)

s2={"John",1,(3,5,6)}
print(s|s2)