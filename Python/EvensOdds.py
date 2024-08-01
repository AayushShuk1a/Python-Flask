even=[]
odd=[]

while True:
    choice=input("Enter A to Add and Q to Quit: ").lower()

    if choice=='q':
        break

    n=int(input("Enter Number To Be Added: "))

    if n%2==0:
        even.append(n)
    else:
        odd.append(n)


print(even)
print(odd)