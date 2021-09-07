userInput = input("Username :")
passInput = input("Password :")
amount_Apple = 0
amount_Banana = 0
amount_Orange = 0

if userInput == "Dev_admin" and passInput == "admin" :
    print("login Success")
    print("----------------------")
    print("Welcome to nShop")
    print("What product would you like to get?")
    print(" 0. notthing else       price x1 kg : 0 THB")
    print(" 1. Apple               price x1 kg : 40 THB")
    print(" 2. Banana              price x1 kg : 30 THB")
    print(" 3. orange              price x1 kg : 50 THB")
    product_Selected = int(input("Please choose product :"))
    while product_Selected != 0 :
        if product_Selected == 1 :
            amount_Apple = int(input("Amount of apple (kg):"))
            product_Selected = int(input("Please choose product :"))    
        elif product_Selected == 2 :
            amount_Banana = int(input("Amount of banana (kg) :"))
            product_Selected = int(input("Please choose product :"))    
        elif product_Selected == 3 :
            amount_Orange = int(input("Amount of orange (kg) :"))
            product_Selected = int(input("Please choose product :"))
        result = (40 * amount_Apple)+(30 * amount_Banana)+(50 * amount_Orange)
        print("Total price :", result ,"THB")         
else :
    print("login Error , Please Check your Username and Password !")