number_Count = int(input("Please Enter Number :"))
space = number_Count

for i in range(number_Count) :
    space = space -1
    print(" "*space,"*"*((i * 2) + 1))

