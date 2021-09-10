# Return part 2

totalprice = int(input("Please Enter Total Price :"))

def vatCalculate(totalprice) :
    result = totalprice + (totalprice * 7 / 100)
    return result

print(vatCalculate(totalprice))