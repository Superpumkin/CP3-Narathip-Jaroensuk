menu_List = []
price_List = []


def showBill() :
    totalPrice = 0
    print("--------- nshop -----------")
    for number in range(len(menu_List)) :
        print(menu_List[number],price_List[number],"THB")
        totalPrice += int(price_List[number])
    print("Total :", totalPrice ,"THB")


while True :
    menu_Name = input("Please Enter Menu :")
    if (menu_Name.lower() == "exit") :
        break
    else :
        menu_Price = input("Please Enter Price :")
        menu_List.append(menu_Name)
        price_List.append(menu_Price)

showBill()