DB_PASSWORD = "Georgia"
MAX_TRIES = 3


for i in range(MAX_TRIES):
    input_password = input("Please enter password: ")
    if input_password == DB_PASSWORD:
        print("Hello from Georgia")
        break
    else:
        print("Password was not correct. Try again - ")
else:
    print("you are blocked")

