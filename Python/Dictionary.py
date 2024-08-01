peoples={"Rolf":24,"Sam":33,"Ron":45}
peoples["ronny"]=44

print(peoples["Rolf"])
print(peoples)

for name,age in peoples.items():
    print(f"{name}: {age}")

#List Of Dictionary
Movies=[
    {"name":"The Green Book","rating":8},
    {"name":"Lion","rating":9},
    {"name":"Joker","rating":10}
]

for movie in Movies:
    name=movie["name"]
    rating=movie["rating"]
    print(f"{name}: {rating}")

