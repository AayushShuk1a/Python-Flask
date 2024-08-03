def divide(dividend,divisor):
    if(divisor==0):
        raise ZeroDivisionError("Divisor Cannot Be Zero")
    
    return dividend/divisor

grades=[78,76,87,97,67]

print("Welcome!!")

try:
    average=divide(sum(grades),len(grades))
except ZeroDivisionError as e:
    print("There are no grades in your list")
else:
    print(f"Average is: {average}")
finally:
    print("Closing!!")
