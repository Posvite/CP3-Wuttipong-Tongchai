menuList = []
def showBill():
    total = 0
    print("SHOP".center(20, "-"))
    for number in range(len(menuList)):
        total += int(menuList[number][1])
        print(menuList[number][0], menuList[number][1])
    print("ยอดรวม %s"%(total))
while True:
    menuName = input("please Enter Menu >")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price >")
        menuList.append([menuName,menuPrice])

print(menuList)
showBill()

