def celVat(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

print(celVat(int(input("Price = "))))