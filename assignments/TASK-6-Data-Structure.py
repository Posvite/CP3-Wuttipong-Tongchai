number = int(input())
avg_sum = 0.0
for i  in range(number):
    avg_sum += float(input())
print("%.2f" %(avg_sum/number))