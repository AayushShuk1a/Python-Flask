users=[
    (0,"Rolf","hello123"),
    (1,"Ron","test123"),
    (2,"Sam","Sam123")
]


user_dictionary={user[1]:user for user in users}

username=(input("Enter Username: "))
password=input("Enter Password: ")

if username in user_dictionary:
    _,user,passw=user_dictionary[username]
    if passw==password:
        print("Welcome!!")
    else:
        print("Wrong Password")
else:
    print("Wrong UserName")


