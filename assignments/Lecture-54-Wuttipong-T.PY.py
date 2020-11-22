def login():
    username = input("ID >")
    password = input("Password >")
    if username == "member" and password == "123":
        return showMenu()
    else:
        print("ข้อมูลผิด")
def showMenu():
    print("Done !")
    print("-----Jam3s-----")
    print("[1] Vat Calculator")
    print("[2] Price Calculator")
    return MenuSelect()
def MenuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return VatCalculate(int(input("Price >")))
    elif userSelected == 2:
        return priceCalculate()
    else:
        print("กรอกตัวเลขผิด")
def VatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price >"))
    price2 = int(input("Second Product Price >"))
    return VatCalculate(price1 + price2)

login()