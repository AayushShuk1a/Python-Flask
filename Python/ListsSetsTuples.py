#Sets,Tuples & Lists

l=["John","Gwen","Ben"]
t=("John","Gwen","Ben")
s={"John","Gwen","Ben"}

print(l[0])

l.append("Ron")
l.remove("Gwen")
print(l)

s.add("Ron")
print(s)

#Tuples cannot be modified so no CRUD
#Sets Does not contain Duplicates & set does not have order so you cannot use s[0]
#List are same as ArrayList

