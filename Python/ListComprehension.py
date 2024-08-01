num=[1,3,4,6]
doubled=[x*2 for x in num]
print(doubled)

peoples=["john","johnny","doe","jiten","Sam"]
start_p=[people for people in peoples if people.startswith("j")]
print(start_p)
