arry_list = []
count = int(input())
sum = 0.0
text_items = ''
for i in range(count):
    arry_list.append(float(input()))
for x in arry_list:
    sum += x

if count == 1:
    text_items = "Item"
else:
    text_items = "Items"

print(f"COUNT : "
      f"{count} "
      f"{text_items}")
print("SUM : %.2f"
      %sum)
print("Min : %.2f"
      %min(arry_list))
print("Max : %.2f"
      %max(arry_list))
print("AVG : %.2f"
      %(sum/count))