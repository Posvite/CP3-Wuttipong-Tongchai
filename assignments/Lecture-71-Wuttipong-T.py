menuList = []
priceList = []
def showBill():
    print("SHOP".center(20, "-"))
    for number in range(len(menuList)):
        total = 0
        print(menuList[number],priceList[number])
        for i in priceList:
            total += int(i)
    print("ผลรวมทั้งหมด %s"%(total))
while True:
    menuName = input("please Enter Menu >")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price >")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()

