systemMenu = {'ข้าวมันไก่':50, 'ข้าวไก่ทอด':50, 'ข้าวผัด':60, 'ข้าวหมกไก่':50}
menuList = []
def showBill():
    total = 0
    print("SHOP".center(20, "-"))
    for number in range(len(menuList)):
        total += int(menuList[number][1])
        print(menuList[number][0],menuList[number][1])
    print("ยอดรวม %s"%(total))
while True:
    menuName = input("please Enter Menu >")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showBill()

