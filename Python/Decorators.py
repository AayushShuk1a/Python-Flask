import functools
user={"username":"Jose","role":"admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["role"]=="admin":
            return func()
        else:
            print("You need to be admin")

    return secure_function


@make_secure
def getPassword():
    return "1234"

print(getPassword())