#Login
username = input("ID >")
password = input("Password >")
#Price Product
coka = 10
popcorn = 5
coffee = 15
water = 12


if username == "member" and password == "123":
    print("เข้าสู่ระบบ", username)
    print("รายการสินค้า")
    print("[1]","Coka",coka,"THB")
    print("[2]","Popcorn",popcorn,"THB")
    print("[3]","Coffee",coffee,"THB")
    print("[4]","Water",water,"THB")
    product = int(input("เลือกสินค้าที่ต้องการซื้อได้ระบุหมายเลข 1 - 2 - 3 - 4 >"))
    if product == 1:
        print("ได้เลือกซื่อ Coka")
        coka_amount = int(input("ระบุจำนวนที่ต้องการซื้อ >"))
        print("ยอดที่ต้องชำระทั้งหมด",coka * coka_amount)
    elif product == 2:
        print("ได้เลือกซื้อ Popcorn")
        popcorn_amount = int(input("ระบุจำนวนที่ต้องการซื้อ >"))
        print("ยอดที่ต้องชำระทั้งหมด",popcorn * popcorn_amount)
    elif product == 3:
        print("ได้เลือกซื้อ Coffee")
        coffee_amount = int(input("ระบุจำนวนที่ต้องการซื้อ >"))
        print("ยอดที่ต้องชำระทั้งหมด", coffee * coffee_amount)
    elif product == 4:
        print("ได้เลือกซื้อ Water")
        water_amount = int(input("ระบุจำนวนที่ต้องการซื้อ >"))
        print("ยอดที่ต้องชำระทั้งหมด",water * water_amount)
    else:
        print("ระบุหมายเลขไม่ถูกต้อง")
else:
    print("ข้อมูลไม่ถูกต้อง")