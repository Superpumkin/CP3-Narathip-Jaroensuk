def login() :
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "dev" :
        print("login Success")
        return showMenu()
    else :
        print("login Error ,please check your username and password")
        return login()

def showMenu() :
    print(" Welcome to nShop")
    print(" 1. Vat Calculator")
    print(" 2. Price Calculator ")
    print(" 3. Exit ")
    return menuSelect()

def menuSelect() :
    userSelected = int(input("choice :"))
    if userSelected == 1 :
        amount = int(input("Please Enter Total Price :"))
        return vatCalculate(amount)
    elif userSelected == 2 :
        return priceCalculate()
    elif userSelected == 3 :
        return exit()
    else :
         return showMenu()

def vatCalculate(totalprice) :
    vat = 7 / 100
    result = totalprice + (totalprice * vat)
    print("Total Price is :", result)

def priceCalculate() :
    price_1 = int(input("First Product Price :"))
    price_2 = int(input("Second Product Price :"))
    return vatCalculate(price_1 + price_2)

login()