def login():
    # n=1 and while n!=0 can be used to run infinite times
    while True:  # True is used to run the program infinite times
        username = input("enter your username:")
        password = input("enter your password:")
        if username == password:
            print("you logged in successfully.")
            break
        else:
            print("failed to login")


login()
