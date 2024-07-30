inList={"Green Book","Joker","Your Name"}

userInput=input("Enter Movie: ")

if userInput in inList:
    print("Movie Already in The List")
else:
    inList.add(userInput)
    print(inList)