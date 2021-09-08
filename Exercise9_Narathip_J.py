print("Please login")
userInput = input("Username :")
passInput = input("Password :")

while userInput != "admin" or passInput != "OAT" :
    print("Please check your username or password again !")
    userInput = input("Username :")
    passInput = input("Password :")
print("Welcome to webpage zone ")
