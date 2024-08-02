def multiply(*args):
    total=1
    for arg in args:
        total*=arg

    return total

def apply(*args,operator):
    if operator=="+":
        return sum(args)
    elif operator=="*":
        return multiply(*args)
    else:
        return "Invalid Operator"


print(apply(1,3,4,8,operator="*"))
