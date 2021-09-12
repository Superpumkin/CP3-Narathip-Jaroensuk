menu_List = []
system_Menu = {"ข้าวหมกไก่": 45 , "ข้าวมันไก่": 40 , "ข้าวมันไก่ผสม": 50 , "ข้าวมันไก่พิเศษ": 45}

def showBill() :
    totalPrice = 0
    print("--------- My Food -----------")
    for number in range(len(menu_List)) :
        print(menu_List[number][0],menu_List[number][1] ,"THB")
        totalPrice += int(menu_List[number][1])
    print("Total :",totalPrice,"THB")

while True :
    menu_Name = input("Please Enter Menu :")
    if (menu_Name.lower() == "exit") :
        break
    else :
        menu_List.append([menu_Name , system_Menu[menu_Name]])

showBill()