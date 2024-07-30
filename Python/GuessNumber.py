num=7



while True:
    userInput=input("Enter (y/n): ")
    if userInput=='n':
        break
    n=int(input("Enter Your Number: "))
    if num==n:
        print("Correct Number")
        break
    elif abs(num-n)==1:
        print("You were Off By 1")
    else:
        print("Wrong Number")